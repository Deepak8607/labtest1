import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as ls
trading_volume=np.array(126)
days=np.array(252)
trading_volume=np.random.rand(0,126)
print(trading_volume)
print(days)

weekly_trading=np.sum(trading_volume)
print(weekly_trading)
def low_pass_filter():
smooth_trading=ls.lowpass(trading_Volume);
plt.title(plot of trading chart)
plt.plot(smooth_trading,color="r",label="Plot of trading values")
plt.plot(days,label="no of days")
plt.legend()
plt.show()



