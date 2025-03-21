import streamlit as st
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
st.image("pages/coral.png",caption="Graph to show Coral Bleaching graph over the years")
st.write("This shows that coral bleaching is becoming more serious each year and it will reach 90% coral bleaching by 2050")
st.write("Now you may ask: Eh, coral reefs is in the sea, not the land, is not gonna affect us. Rightttt????")
st.write("Well the truth is.. NO!!!! Coral reefs provide fishes and other organisms shelter, find food, reproduce, and rear their young in the many nooks and crannies formed by corals. Without the corals providing all these to the organisms will we get our seafood?")
st.write("Half a billion people rely on coral reefs for food and income. But reefs provide more than food. They also provide protection. Healthy reefs protect land from the damaging effects of tropical storms, shielding the shoreline from waves.")
st.write("Soooo yes, corals very important. Have I convinced you yet?")

code = ''' import matplotlib.pyplot as plt

# Years and coral bleaching percentages
years = [1988, 2009, 2014, 2017, 2018, 2024]
bleaching = [8, 8+14, 8+14, 8+14+65.5, 8+14+65.5, 8+14+65.5]  # Cumulative percentages

# Plot the graph
plt.figure(figsize=(10, 5))
plt.plot(years, bleaching, marker='o', linestyle='-', color='coral', label='Coral Bleaching')

# Labels and title
plt.xlabel('Year')
plt.ylabel('Percentage of Coral Bleaching')
plt.title('Coral Bleaching over the Years')
plt.ylim(0, 100)
plt.grid(True, linestyle='--', alpha=0.6)

# Show the plot
plt.legend()
plt.show() '''
st.code(code, language ="python")
st.caption("This is the code for the graph")

