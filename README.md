# Daily-Return-Autocorrelation
We compute the day/day+1 correlation for several stocks, plot an histogram and test whether it differs from zero using the following model : the vector of daily log returns (R1, ..., Rn) is Gaussian, the mean is zero and the covariance matrix SIGMA has the same coefficient sigma^2 on its diagonal. Our null hypothesis is that R1, ..., Rn are actually independant, under which one has the asymptotic approximation 

sqrt(n)*Corr ~ N(0, 1). 

Such an asymptotic limit comes from the central limit theorem applied to the sample covariance. Note that variables (RiRi+1) are not necessarily independent but uncorrelated under the null hypothesis, which is sufficient for the asymptotic result.

The negative correlation observed for most of stocks is statistically significant.

We plot histogram whose xaxis represents the list of stocks and yaxis represents the empirical correlation. Error bars do not represent uncertainty but delimitate rejection region.
