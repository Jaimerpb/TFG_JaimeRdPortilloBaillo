using OrdinaryDiffEq, Plots, VectorFieldPlots

g(x₁,x₂)=[x₂,-x₁]
x₁s=-10.0:0.5:10.0
x₂s=-10.0:0.5:10.0

x₁s_phase=-10.0:1:10.0
x₂s_phase=-10.0:1:10.0
#Plot the vector field
# fig= plot_vector_field(x₁s, x₂s, g, scale=0.5)
#Plotear el diagrama de fases del sistema resultante
fig=plot_phase_portrait(x₁s_phase,x₂s_phase, g, 10.0)
xlabel!("x₁")
ylabel!("x₂")
xlims!(-10, 10)
ylims!(-10, 10)
display(fig)