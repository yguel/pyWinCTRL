import subprocess
from ewmh import EWMH

class WinCtrl:
  def __init__(self) -> None:
    _win = []
  
  def get_all_windows_with_wmctrl(self):
    result = subprocess.run(["wmctrl", "-l"], stdout=subprocess.PIPE)
    entries = result.stdout.decode('utf-8').split("\n")
    """
        Each window entry is a 4-tuple: 
            (id, desktop number, host, window title)
        * id is a hexadecimal number that can be used to identify the window.
        * desktop number is the number of the desktop that the window is on.
        * host is the hostname of the machine that the window is on.
        * window title is the title of the window.
    """
    splitted = [tuple(entry.split()[0:4]) for entry in entries if entry]
    self._win = []
    for entry in splitted:
        self._win.append({
            "id": entry[0],
            "desktop": entry[1],
            "host": entry[2],
            "title": entry[3]
        })
    return self._win
  
  def get_all_windows_with_ewmh(self):
    ewmh = EWMH()
    self._win = []
    client_list = ewmh.getClientList()
    for win in client_list:
        self._win.append({
            "window_object": win,
            "desktop": ewmh.getWmDesktop(win),
            "title": ewmh.getWmName(win).decode('utf-8')
        })
    return self._win
  
  def get_all_windows(self):
    return self.get_all_windows_with_ewmh()
  
  def maximize_window_with_wmctrl(self, win_id: str):
    subprocess.run(["wmctrl", "-i", "-r", win_id, "-b", "add,maximized_vert,maximized_horz"])  
  
  def maximize_window_with_ewmh(self, win_obj, demand_attention=False):
    ewmh = EWMH()
    ewmh.setActiveWindow(win_obj)
    ewmh.setWmState(win_obj, 1, '_NET_WM_STATE_MAXIMIZED_VERT')
    ewmh.setWmState(win_obj, 1, '_NET_WM_STATE_MAXIMIZED_HORZ')
    if demand_attention:
        ewmh.setWmState(win_obj, 1, '_NET_WM_STATE_DEMANDS_ATTENTION')
    else:
        ewmh.setWmState(win_obj, 0, '_NET_WM_STATE_DEMANDS_ATTENTION')
    ewmh.display.flush()
  
  def get_windows_by_name_filter(self, ends_with: str):
    self.get_all_windows()
    return [win for win in self._win if win["title"].endswith(ends_with)]
  
  def maximize_windows_by_name_filter(self, ends_with: str):
    ewmh = EWMH()
    windows = self.get_windows_by_name_filter(ends_with=ends_with)
    for win in windows:
      self.maximize_window_with_ewmh(win["window_object"])
    ewmh.display.flush()
  
  def remove_demands_attention(self, win_obj):
    ewmh = EWMH()
    ewmh.setWmState(win_obj, 0, '_NET_WM_STATE_DEMANDS_ATTENTION')
    ewmh.display.flush()
  
  def remove_demands_attention_by_name_filter(self, ends_with: str):
    ewmh = EWMH()
    windows = self.get_windows_by_name_filter(ends_with=ends_with)
    for win in windows:
      self.remove_demands_attention(win["window_object"])
    ewmh.display.flush()