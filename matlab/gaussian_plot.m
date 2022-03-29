x = 0:1/100:10;
sigmas = 0.5:0.5:1.5;
mu = 5;
ys = [];
for sigma = sigmas 
    y = (1/sqrt(2*pi*sigma^2))*exp(-(x-mu).^2/(2*sigma^2));
    ys = [ys;y];
end
plot(x,ys(1,:),'r--',x,ys(2,:),'b-.',x,ys(3,:),'g')
xlabel('x')
ylabel('\phi(x-5,\sigma)')
legend('0.5','1.0','1.5')




 