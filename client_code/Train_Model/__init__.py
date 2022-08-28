from ._anvil_designer import Train_ModelTemplate
from anvil import *

class Train_Model(Train_ModelTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
