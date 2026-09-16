# Continuous-Time Signal Convolution Using Python

A beginner-friendly **Signals & Systems** project that demonstrates the numerical computation and visualization of the convolution of two continuous-time signals using Python.

## 📌 Overview

Convolution is a fundamental operation in Signals & Systems and is widely used in areas such as signal processing, communication systems, and control systems.

In this project, the convolution of a continuous-time signal with a unit-step-based impulse response is computed numerically using **SciPy's `quad()` integration function** and visualized using **Matplotlib**.

The project was created to connect theoretical concepts from Signals & Systems with practical Python implementation.

## 📐 Mathematical Background

The convolution of two continuous-time signals is defined as:

$$
y(t) = x(t) * h(t)
$$

$$
y(t) = \int_{-\infty}^{\infty} x(\tau)h(t-\tau)d\tau
$$

For this project:

$$
x(t) =
\begin{cases}
e^t, & t < 0 \\
0, & t \geq 0
\end{cases}
$$

and

$$
h(t) = u(t-1)
$$

where \(u(t)\) is the unit step function.

The convolution is evaluated numerically for multiple values of \(t\).

## 🛠️ Technologies Used

* **Python**
* **NumPy** — numerical operations and generation of sample points
* **SciPy** — numerical integration using `scipy.integrate.quad`
* **Matplotlib** — visualization of the resulting convolution signal

## ⚙️ How It Works

The implementation follows these steps:

1. Define a unit step function.
2. Define the continuous-time input signal \(x(t)\).
3. Define the signal \(h(t)\).
4. Construct the convolution integral.
5. Numerically evaluate the integral using `scipy.integrate.quad()`.
6. Generate sample time values using NumPy.
7. Plot the resulting convolution using Matplotlib.

## 📊 Result

The computed convolution produces a signal that approaches 1 exponentially and becomes constant after \(t=1\).

The analytical result is:

$$
y(t) =
\begin{cases}
e^{t-1}, & t < 1 \\
1, & t \geq 1
\end{cases}
$$

The numerical implementation can therefore be compared with the theoretical result to verify the computation.

## 🚀 Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/signal-convolution-python.git
cd signal-convolution-python
```

### 2. Install the required libraries

```bash
pip install numpy scipy matplotlib
```

### 3. Run the program

```bash
python convolution.py
```

A plot showing the computed convolution will be generated.

## 📚 What I Learned

Through this project, I practiced:

* Implementing mathematical functions in Python
* Numerical integration using SciPy
* Working with continuous-time signal concepts
* Applying the convolution integral computationally
* Generating and visualizing numerical data with Matplotlib
* Connecting Signals & Systems theory with programming

## 🔮 Future Improvements

Possible improvements include:

* Compare numerical and analytical convolution on the same graph
* Add more types of signals
* Implement discrete-time convolution
* Add interactive signal parameters
* Visualize \(x(t)\), \(h(t)\), and \(y(t)\) separately
* Build a small GUI for experimenting with convolution

## 👨‍💻 Author

**[Harsh Sharma]**

ECE Student | Learning Python & Signal Processing

---

⭐ If you find this project useful, feel free to explore the repository.
