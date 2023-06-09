# Spherical collapse

## <small>Examining the physics behind a new scheme for laser fusion</small>

___

I examined physics underpinning laser fusion by simulating collapsing shocks through bounce and reflection at the origin, using high performance computing techniques

**Skills employed:**  Hydrodynamics, time series analysis, mathematics, large dataset analysis, Linux, parallel computing, C++, Python, Cython, Matplotlib, NumPy, SciPy

<div class='tallvideoWrapper'><iframe src='https://www.youtube.com/embed/w9z8Mn9ABJE'></iframe></div>

*Example simulation output, the lower half showing the shock front and top half showing a cut through of the hydrodynamic data.*

## Researching collapsing shockwaves

Using high performance computing techniques, I examined physics underpinning laser fusion by simulating collapsing shocks through bounce and reflection at the origin. This was as part of my academic research.

I designed, implemented and interpreted these simulations, in C++ and Fortran, parallel on 100s of cores, adapting an external code. I also designed and constructed parallel algorithms for data analysis, in compiled Python, processing data in parallel up to 100s Gb/min.

This campaign of simulations was successful, leading to publications, talks at international conferences and further contracts with the research group.

### Physics Summary

Laser fusion is a potential method of generating electricity using lasers to compress hydrogen fuel.   Converging and reflected shocks are central to laser fusion, these shocks compressing and heating the fuel, reflecting many times at collapse.  Once heated, the fuel should burn and give out energy.

Motivated by recent results contradicting an earlier mathematical model, I constructed a computer model to examine the fundamental principles of these reflected shock models.  I found the cause of the contradiction, expanded the model and found many new bits of physics, including an intermediate type of instability not seen in this situation before.

My supervisor and I published 2 papers from this research, and with a little additional work there is the option of another 2 or 3.  The first paper is in the high impact PRL journal, the second paper is in the very credible Physics of Plasmas journal.

(It also informed most of the research in my thesis, I'll link to it when it is up, but honestly, the interesting results are in a much more concise form in the papers.)

### Computing Summary

The most resource intensive and difficult computational challenge was finding the shock front, these difficulties compounded when transferring to 3D - the algorithm needed to explore 10s of gigabytes of often noisy data, output from the simulation a few times a minute.

I designed and implemented this algorithm for finding the shock front, and optimised the most resource intensive parts of this Python code using a range of techniques, including exploiting natural symmetries in the geometry of the problem and the requirement that the shock front position was smoothly varying. I also used computational techniques, firstly rewriting the code in compiled Python (Cython), ensuring the code ran in stride and ensuring that the code could be simply vectorised by the compiler and libraries.

I finally wrote it in such a way that could be run in parallel, and this parallelisation was effective on up to 15 nodes, after which it was processing the data faster than the simulation was producing it (a rate of 100s Gb/min).
