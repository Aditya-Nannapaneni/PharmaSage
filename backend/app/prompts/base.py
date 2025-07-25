"""
Base utilities and classes for prompt management.
"""

class PromptTemplate:
    """Base class for prompt templates with variable substitution."""
    
    def __init__(self, template):
        self.template = template
        
    def format(self, **kwargs):
        """Format the prompt template with the given variables."""
        return self.template.format(**kwargs)
