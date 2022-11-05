from ._anvil_designer import Display_SimulationTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Display_Simulation(Display_SimulationTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def start_simulation_btn_click(self, **event_args):
    # get initial position and velocity of each body
    pass




