# Noodles

The goal of NOODLES is to provide a framework for building real-time, collaborative, 3D data visualizations. Imagine if you are a researcher and you want to visualize the data from your windfarm simulation. If you wanted a 3D visualization you would have to create a bespoke solution for VR headsets, AR glasses, web browsers, etc. NOODLES establishes a protocol that is agnostic to the hardware and allows for real-time, collaborative, 3D data visualizations.

![Noodles](images/mesh.png)

My work focused on implementing the protocol in Python and developing tools to make it as easy as possible for researchers to visualize their data. During my time at NREL, I developed three Python packages that enabled immersive 3D visualization workflows.

## Penne

A client library that allows users to join a NOODLES session and view 3D data in real-time.

[View the Website →](https://insightcenternoodles.github.io/Penne/)
[View on GitHub →](https://github.com/InsightCenterNoodles/Penne)

## Rigatoni

A server library that allows users to create NOODLES sessions and share 3D data in real-time.

[View the Website →](https://insightcenternoodles.github.io/Rigatoni/)
[View on GitHub →](https://github.com/InsightCenterNoodles/Rigatoni)

## Orzo

A 3D rendering application built from scratch using ModernGL and Python. It has been used regularly by researchers for testing and developing NOODLES sessions. I built the shaders from scratch using GLSL and linear algebra, and I tested the application on geometries as large as 12M triangles.

[View the Website →](https://insightcenternoodles.github.io/Orzo/)
[View on GitHub →](https://github.com/InsightCenterNoodles/Orzo)


For more NOODLES-related projects, see the [InsightCenterNoodles collection](https://github.com/InsightCenterNoodles).
