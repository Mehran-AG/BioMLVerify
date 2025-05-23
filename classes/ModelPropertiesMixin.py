import numpy as np

class ModelPropertiesMixin:

    @property
    def ID(self):
        """Getter for ID"""
        return self._ID

    @ID.setter
    def ID(self, new_ID):
        self._ID = str(new_ID)

    
    @property
    def compartments(self):
        '''Getter for compartments'''
        return self._compartments
    
    @compartments.setter
    def compartments(self, new_compartments):
        '''Setter for compartments - Ensures it is a list'''
        if not isinstance(new_compartments, list):
            raise ValueError("compartments must be stored in a list")
        self._compartments = new_compartments




    @property
    def reactions(self):
        '''Getter for reactions'''
        return self._reactions
    
    @reactions.setter
    def reactions(self, new_reactions):
        '''Setter for reactions - Ensures it is a list'''
        if not isinstance(new_reactions, list):
            raise ValueError("reactions must be stored in a list")
        self._reactions = new_reactions

    @property
    def species(self):
        '''Getter for species'''
        return self._species
    
    @species.setter
    def species(self, new_species):
        '''Setter for species - Ensures it is a list'''
        if not isinstance(new_species, list):
            raise ValueError("species must be stored in a list")
        self._species = new_species

    @property
    def parameters(self):
        '''Getter for parameters'''
        return self._parameters
    
    @parameters.setter
    def parameters(self, new_parameters):
        '''Setter for parameters - Ensures it is a list'''
        if not isinstance(new_parameters, list):
            raise ValueError("parameters must be stored in a list")
        self._parameters = new_parameters


    @property
    def function_definitions(self):
        '''Getter for function_definitions'''
        return self._function_definitions
    
    @function_definitions.setter
    def function_definitions(self, new_definitions):
        '''Setter for function_definitions - Ensures it is a list'''
        if not isinstance(new_definitions, list):
            raise ValueError("function definitions must be stored in a list")
        self._function_definitions = new_definitions


    @property
    def kinetic_rate_constants_vector(self):
        return self._kinetic_rate_constants_vector
    
    @kinetic_rate_constants_vector.setter
    def kinetic_rate_constants_vector(self, vec):
        if isinstance(vec, np.ndarray):
            self._kinetic_rate_constants_vector = vec
        else:
            raise ValueError("Input must be a numpy 1D array")