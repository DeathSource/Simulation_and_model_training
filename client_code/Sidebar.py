from ._anvil_designer import SidebarTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .Create_Simulation import Create_Simulation
from .Train_Model import Train_Model

class Sidebar(SidebarTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.create_simulation_lnk.tag.form_to_open = Create_Simulation()
    self.train_model_lnk.tag.form_to_open = Train_Model()
    self.content_panel.add_component(Create_Simulation())
    
    # Any code you write here will run before the form opens.
  def navigation_click(self, **event_args):
    form_to_open = event_args['sender'].tag.form_to_open
    self.content_panel.clear()
    self.content_panel.add_component(form_to_open)
    pass






