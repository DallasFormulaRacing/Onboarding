# Plot Dataframes as a line graph
rpmPlot = px.line(rpm, x = "Time (Sec)", y = "RPM", title = "RPM over Time");

# Show Data on Graph
rpmPlot.show()