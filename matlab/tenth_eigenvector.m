npoints = 10
twos = 2*ones(npoints,1);
diagonal_twos = diag(twos);
negative_ones = -1*ones(npoints-1,1);
upper_diag_ones= diag(negative_ones,1);
lower_diag_ones= diag(negative_ones,-1);
prefactor = 1/(2*(1/(npoints+1))^2);
H = prefactor * (diagonal_twos + upper_diag_ones + lower_diag_ones);
[eigenvectors,eigenvalues] = eig(H)
xvalues = linspace(1/(npoints+1), npoints/(npoints+1), npoints);
yvalues = eigenvectors(:,1)
xvalues2 = linspace(0,1)
yvalues2 = sqrt(2)*sin(pi*xvalues2)
plot (xvalues,yvalues,xvalues2,yvalues2)