
# struktuur: "taime nimi": [["sobiv taim1", "sobiv taim2"], ["OK taim 1", "ok taim 2"], ["halb taim1", "halb taim2"]]
_dict = {
    "taim1": [["taim2", "taim3"], ["taim4", "taim5"], ["taim6", "taim7"]],
    "taim2": [["taim3", "taim4"], ["taim5", "taim6"], ["taim7", "taim1"]],
    "taim3": [["taim4", "taim5"], ["taim6", "taim7"], ["taim1", "taim2"]],
    "taim4": [["taim5", "taim6"], ["taim7", "taim1"], ["taim2", "taim3"]],
    "taim5": [["taim6", "taim7"], ["taim1", "taim2"], ["taim3", "taim4"]],
    "taim6": [["taim7", "taim1"], ["taim2", "taim3"], ["taim4", "taim5"]],
    "taim7": [["taim1", "taim2"], ["taim3", "taim4"], ["taim5", "taim6"]]
}
