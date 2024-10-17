import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# 1. データの生成
np.random.seed(0)  # 再現性のためのシード
mu_true = 3.238748237832  # 真の平均
sigma2_true = 2.2384783274  # 真の分散
n = 1000  # データの数

data = np.random.normal(mu_true, np.sqrt(sigma2_true), n)

# 2. 事前分布の設定
mu_0 = 0
tau2 = 1
alpha = 2
beta = 1

# 3. コンディショナル分布の計算とGibbsサンプリングの実行
iterations = 1000
mu_samples = np.zeros(iterations)
sigma2_samples = np.zeros(iterations)

# 初期値
mu_current = np.mean(data)
sigma2_current = np.var(data)

for i in range(iterations):
    # mu のサンプリング
    mu_n = (mu_0/tau2 + np.sum(data)/sigma2_current) / (1/tau2 + n/sigma2_current)
    tau2_n = 1 / (1/tau2 + n/sigma2_current)
    mu_current = np.random.normal(mu_n, np.sqrt(tau2_n))
    
    # sigma2 のサンプリング
    alpha_n = alpha + n/2
    beta_n = beta + 0.5 * np.sum((data - mu_current)**2)
    sigma2_current = 1 / np.random.gamma(alpha_n, 1/beta_n)
    
    mu_samples[i] = mu_current
    sigma2_samples[i] = sigma2_current

# 推定値の計算
mu_est = np.mean(mu_samples)
sigma2_est = np.mean(sigma2_samples)
mu_sd = np.std(mu_samples)
sigma2_sd = np.std(sigma2_samples)

# 信用区間の計算
mu_ci_99 = np.percentile(mu_samples, [0.5, 99.5])
mu_ci_95 = np.percentile(mu_samples, [2.5, 97.5])
mu_ci_90 = np.percentile(mu_samples, [5, 95])

sigma2_ci_99 = np.percentile(sigma2_samples, [0.5, 99.5])
sigma2_ci_95 = np.percentile(sigma2_samples, [2.5, 97.5])
sigma2_ci_90 = np.percentile(sigma2_samples, [5, 95])

# 信用区間が0を含むかどうかのチェック
mu_star_99 = "***" if mu_ci_99[0] > 0 or mu_ci_99[1] < 0 else ""
mu_star_95 = "**" if mu_ci_95[0] > 0 or mu_ci_95[1] < 0 else ""
mu_star_90 = "*" if mu_ci_90[0] > 0 or mu_ci_90[1] < 0 else ""

sigma2_star_99 = "***" if sigma2_ci_99[0] > 0 or sigma2_ci_99[1] < 0 else ""
sigma2_star_95 = "**" if sigma2_ci_95[0] > 0 or sigma2_ci_95[1] < 0 else ""
sigma2_star_90 = "*" if sigma2_ci_90[0] > 0 or sigma2_ci_90[1] < 0 else ""

# 結果の表示
results = {
    'Parameter': ['μ', 'σ²'],
    'True Value': [mu_true, sigma2_true],
    'Posterior Mean': [mu_est, sigma2_est],
    'Std Dev': [mu_sd, sigma2_sd],
    '99% CI': [f"{mu_ci_99} {mu_star_99}", f"{sigma2_ci_99} {sigma2_star_99}"],
    '95% CI': [f"{mu_ci_95} {mu_star_95}", f"{sigma2_ci_95} {sigma2_star_95}"],
    '90% CI': [f"{mu_ci_90} {mu_star_90}", f"{sigma2_ci_90} {sigma2_star_90}"]
}

import pandas as pd

results_df = pd.DataFrame(results)

# 表示
print(results_df)