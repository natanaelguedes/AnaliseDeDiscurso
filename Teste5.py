


import plotly.graph_objects as go
from matplotlib import pyplot as plt
DiversidadeArtisticas=['Artesanatos','danças',  'cantos']
espiritualidade = ['Diversidade de rituais', 'Formas de manifestações espirituais']
sabereslocais=['Medicina indigena','Parteiras','rezadeiras/ benzedoras','Simbolos de proteção','Valorizacao da oralidade e saberes ancestrais','Valorizacao dos sinais da natureza']
fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[20,11,10,30,30,30],
    theta=DiversidadeArtisticas,
    fill='toself',
    name='Diversidade de expressões culturais artisticas',
    fillcolor="red", opacity=0.6, line=dict(color="red")

))

fig.add_trace(go.Scatterpolar(
    r=[19,36,10,40,20,30],
    theta=espiritualidade,
    fill='toself',
    name='espiritualidade',
    fillcolor="orange", opacity=0.6, line=dict(color="orange")

))

fig.add_trace(go.Scatterpolar(
    r=[20,10,8,13,28,43],
    theta=sabereslocais,
    fill='toself',
    name='Saberes locais',
    fillcolor="blue", opacity=0.6, line=dict(color="blue")

))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 50]
        )),
    showlegend=True
)

fig.show()