import plotly.graph_objects as go

categories = ['Artesanatos','Danças','chemical stability',
              'thermal stability', 'device integration']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
      r=[23,0,0 ,0, 0],
      theta=categories,
      fill='toself',
      name='Artesanatos'
))
fig.add_trace(go.Scatterpolar(
      r=[10,0,0, 0,0],
      theta=categories,
      fill='toself',
      name='dancas'
))

fig.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[0, 87]
    )),
  showlegend=True
)

fig.show()