using OrdinaryDiffEq, Plots, VectorFieldPlots

g(x₁ ,x₂ )=[x₂,0*x₁]
x₁s=-5.0:0.5:5.0
x₂s=-5.0:0.5:5.0

x₁s_phase=-5.0:1:5.0
x₂s_phase=-5.0:1:5.0
# Plot the vector field
fig1= plot_vector_field(x₁s, x₂s, g, scale=0.5)
#Plotear el diagrama de fases del diagrama resultante.
fig2=plot_phase_portrait(x₁s_phase,x₂s_phase, g, 10.0)
xlabel!("x₁")
ylabel!("x₂")
xlims!(-10, 10)
ylims!(-10, 10)
display(fig1)
display(fig2)
