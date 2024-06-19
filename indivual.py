


import plotly.graph_objects as go
from matplotlib import pyplot as plt
DiversidadeArtisticas=['Artesanatos','cantos',  'danças']
saberes=['teste1','teste2',  'teste3']

fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[23,11,10],
    theta=DiversidadeArtisticas,
    fill='toself',
    name='Diversidade de expressões culturais artisticas',
    fillcolor="red", opacity=0.6, line=dict(color="red")

))
fig.add_trace(go.Scatterpolar(
    r=[80,18,20],
    theta=saberes,
    fill='toself',
    name='Teste',
    fillcolor="DeepPink", opacity=0.6, line=dict(color="DeepPink")

))
plt.yticks([1], ["5"], color="grey", size=7)
plt.yticks([1], ["80"], color="grey", size=7)
plt.ylim(0, 1)
fig.show()