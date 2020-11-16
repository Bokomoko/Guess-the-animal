from browser import document
from loadzoo import *
from salva import *

document["question"].text="Loading zoo. Stand by..."
zoo = loadzoo()
document["question"].text = f"System has loaded { len(zoo) } animals" 
    
def bind_click(ev):
  print("Clicked")
  document["question"].text=""
  document["resposta"].style.display = "inline"

document["sim"].bind("click", bind_click)
document["nao"].bind("click", bind_click)
