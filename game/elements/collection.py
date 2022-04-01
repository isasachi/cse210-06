class Collection:
    """A collection of entities."""

    def __init__(self):
        """Constructs a new entity."""
        self._entitites = {}
        
    def add_entity(self, group, entity):
        """Adds an entity to the given group.
        
        Args:
            group: A string containing the name of the group.
            entity: The instance of entity (or a subclass) to add.
        """
        if group not in self._entitites.keys():
            self._entitites[group] = []
        self._entitites[group].append(entity)

    def clear_entitites(self, group):
        """Clears entities from the given group.
        
        Args:
            group: A string containing the name of the group.
        """
        if group in self._entitites:
            self._entitites[group] = []
    
    def clear_all_entitites(self):
        """Clears all entities."""
        for group in self._entitites:
            self._entitites[group] = []
    
    def get_entitites(self, group):
        """Gets the entities in the given group.
        
        Args:
            group: A string containing the name of the group.

        Returns:
            A list of entity instances.
        """
        results = []
        if group in self._entitites.keys():
            results = self._entitites[group].copy()
        return results
    
    def get_all_entitites(self):
        """Gets all of the entities in the collection.
        
        Returns:
            A list of entity instances.
        """
        results = []
        for group in self._entitites:
            results.extend(self._entitites[group])
        return results

    def get_first_entity(self, group):
        """Gets the first entity in the given group.
        
        Args:
            group: A string containing the name of the group.
            
        Returns:
            An instance of entity.
        """
        result = None
        if group in self._entitites.keys():
            result = self._entitites[group][0]
        return result

    def remove_entity(self, group, entity):
        """Removes an entity from the given group.
        
        Args:
            group: A string containing the name of the group.
            entity: The instance of entity (or a subclass) to remove.
        """
        if group in self._entitites:
            self._entitites[group].remove(entity)