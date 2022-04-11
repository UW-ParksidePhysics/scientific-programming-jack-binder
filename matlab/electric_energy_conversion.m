%I propose to solve the problem of determining how much electrical energy
%is converted into thermal energy inside a variety of wire sizes under a
%certain time period. The reason why this problem interests me is because
%I'm fascinated by energy conversion and the idea of using it to create a 
%more sustainable and practical world. In energy conversion, the variables
%needed are current density, radius of the wire, potential, and time. The 
%main physical principle in this problem is energy conversion. The 
%function needed for this program to operate correctly is an equation that
%can that pull and use at least one input value from a table and then 
%correctly calculate the equation. The vector quantity in this problem 
%would be the current density. I will create my own data table filled with
%different radii values of the wire and will have %to pull each one into 
%the formula. I can visualize this problem through a graph of energy 
%converted vs radius.

%Parameters
current_density = 10.0;
voltage = 2; % volts
time = 120.0; % sec

%Creates matrix of radii
radii = 0.1:0.1:5.0;

%The current = integral of current density times area of cross section of 
%wire
%area of the cross sectional = 2*pi*radius
%since the current density, 2, and pi are constants, they can be taken 
%outside of the integral
%The only thing left inside of the integral is r * dr which becomes (r^2)/2
%The current = (constant/2) * r^2 

%Finding the consant value
constant = (current_density * 2 * pi)/ 2;

%Creates matrix of radii^2
radii_squared = radii.^2;

%Creates matrix of current values
current = constant.* radii_squared;

%Creates matrix of energy values
%energy converted = voltage * time * current
energy = (voltage*time).*current;

%creates graph
plot(radii,energy)
xlabel('Radii(cm)')
ylabel('Thermal Energy Converted')

% Function definitions for simulation solution & visualization
%	Each function contains help text: https://www.mathworks.com/help/matlab/matlab_prog/add-help-for-your-program.html

%
url = 'https://nssdc.gsfc.nasa.gov/planetary/factsheet/';
data = webread(url);
whos data

