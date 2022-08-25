from ._anvil_designer import Model_Training_InputTemplate
from anvil import *

class Model_Training_Input(Model_Training_InputTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    

  def create_simulation_btn_click(self, **event_args):
    open_form("Model_Training_Input")
    pass


