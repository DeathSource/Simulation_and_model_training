from ._anvil_designer import Simulation_InputTemplate
from anvil import *

class Simulation_Input(Simulation_InputTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    
    
  def train_model_btn_click(self, **event_args):
    open_form("Simulation_Input")
    pass


