Pour activer la redirection à la page d'accueil personnalisé de EFFIOS, il faut dans **superset_config.py** ajouter :  
```python
FAB_INDEX_VIEW = "superset.custom.welcome.custom_index.SupersetDashboardIndexView"
```