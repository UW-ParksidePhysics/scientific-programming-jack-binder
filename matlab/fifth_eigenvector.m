twos = 2*ones(5,1);
diagonal_twos = diag(twos);
negative_ones = -1*ones(4,1);
upper_diag_ones= diag(negative_ones,1);
lower_diag_ones= diag(negative_ones,-1);
prefactor = 1/(2*(1/(5+1))^2);
H = prefactor * (diagonal_twos + upper_diag_ones + lower_diag_ones);
[eigenvectors,eigenvalues] = eig(H)
xvalues = linspace(1/(5+1), 5/(5+1), 5);
yvalues = -eigenvectors(:,1)
xvalues2 = linspace(0,1)
yvalues2 = sqrt(2)*sin(pi*xvalues2)
plot (xvalues,yvalues,xvalues2,yvalues2)

