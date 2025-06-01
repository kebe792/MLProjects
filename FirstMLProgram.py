from astropy.io.votable import parse
import pandas as pd
import matplotlib.pyplot as plt

# Load the VOTable file
votable = parse(r'C:\Users\kjfb9\Downloads\selavy-image.i.ThreeLPTs.SB74155.cont.taylor.0.restored.conv.components.xml')

# Extract the first table
table = votable.get_first_table().to_table()

# Convert to pandas DataFrame for easier analysis
df = table.to_pandas()

# Show the first few rows
print(df.head())

plt.figure(figsize=(10, 6))
plt.scatter(df['col_ra_deg_cont'], df['col_dec_deg_cont'], s=5)
plt.xlabel("RA (deg)")
plt.ylabel("Dec (deg)")
plt.title("Detected Radio Components")
plt.gca().invert_xaxis()  # Optional: for astronomical convention
plt.grid(True)
plt.show()

# Example: Color points by spectral index
plt.figure(figsize=(10, 6))
sc = plt.scatter(df['col_ra_deg_cont'], df['col_dec_deg_cont'], 
                 c=df['col_spectral_index'], cmap='coolwarm', s=10)
plt.colorbar(sc, label='Spectral Index')
plt.xlabel("RA (deg)")
plt.ylabel("Dec (deg)")
plt.title("Sky Distribution Colored by Spectral Index")
plt.gca().invert_xaxis()
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

# Define spectral index thresholds
flat_threshold = -0.3
steep_threshold = -0.7

# Filter the DataFrame
flat_spectrum = df[df['col_spectral_index'] > flat_threshold]
steep_spectrum = df[df['col_spectral_index'] < steep_threshold]
intermediate = df[(df['col_spectral_index'] <= flat_threshold) & (df['col_spectral_index'] >= steep_threshold)]

plt.figure(figsize=(10, 6))

# Plot steep spectrum sources (blue)
plt.scatter(steep_spectrum['col_ra_deg_cont'], steep_spectrum['col_dec_deg_cont'],
            c='blue', s=10, label='Steep Spectrum (α < -0.7)', alpha=0.7)

# Plot flat spectrum sources (red)
plt.scatter(flat_spectrum['col_ra_deg_cont'], flat_spectrum['col_dec_deg_cont'],
            c='red', s=10, label='Flat Spectrum (α > -0.3)', alpha=0.7)

# Plot intermediate sources (green)
plt.scatter(intermediate['col_ra_deg_cont'], intermediate['col_dec_deg_cont'],
            c='green', s=10, label='Intermediate Spectrum (-0.7 ≤ α ≤ -0.3)', alpha=0.7)

plt.xlabel("RA (deg)")
plt.ylabel("Dec (deg)")
plt.title("Sky Distribution by Spectral Index Classes")
plt.gca().invert_xaxis()
plt.grid(True)
plt.legend()
plt.show()
