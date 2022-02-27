"""import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as sy
sns.set()
#***********************************************************************************************************************
data=pd.read_csv("E:\Statistics Department\Data scenice\Data Base\Data_Camp_DB\website redsign\mab_data.csv")
print("*"*100)
data.dropna()
data.drop_duplicates()
#delete columns
data.drop("user_id", axis=1, inplace=True)
print("*"*100)
mycrosstab = pd.crosstab(index=data["group"],columns=data["landing_page"],values=data["converted"],aggfunc="count")
print(mycrosstab)
print("*"*100)
print("Chi 2"*20)
print("*"*100)
chi_val, p_val, dof, expected = sy.chi2_contingency(mycrosstab)
alph = 0.05
if p_val>= alph:
    print("H0 is accepted and there is no different" "and pValue is :",p_val)
else:print("H1 is accepted and there is different", "and pValue is :",p_val)
mycrosstab.plot(kind="bar")
plt.show()"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as sy


x=['o1qZG1QH00Q', 'rW7JoYDZ_xk', 'Mn7RzgDDKWY', 'rQYNhWZF1IE', 'i71x6q5dAJk', 'ZrS-Rccep8E', '1GFdluRJbxY', '344bIvljgQw', 'F1Ho0uviLRk', 'xLl0p_EpA4s', '2SefnskEqQs', 'Eieb0YKZXq8', 's0qCJyVlcdo', 'xf70nhDo2aA', '1s9mI5GlYMQ', '2IVitrAnAKU', '3jxBQ-cc0YA', 'T8pi1REm5Xc', 'iqcsXj_o1JM', 'M1zfcVtw7Tk', 'htLqGDF3WbU', 'yARuCJkbWbk', 'EUeZ36cwiac', 'nUrKAigIBEg', '5Cjy49ArRmI', 'bn5t4fepP80', 'w5yzNUG9KJI', '1ABH6Iv6PXo', 'lSXgTKME41k', 'o5twP8BL3TA', 'lMrkJfTFvIs', 'Nw50YZKm0A4', '6mrCrRay3J8', 'gPXMr1OxN2g', 'rAauVMBt4ms', 'mE4z5PvfpGk', '4dhb2jnbyBU', 'wd4lG0Jx6Uo', 'Y6rryDBmfjk', 'ci9mgvRpLlc', 'CyRdQqxdLeg', 'cnIhCQk3zFQ', 'vvEyXUEn6Jk', 'hPSlPhLhCHE', 'EC3tzViefuA', 'wPHHB0MMPfY', '84pVDAwiWj8', 'JvYluNOynlY', 'sYhSpJjQP8w', '2_gGmhqBDpA', 'Ju-QMHLY9cw', 'ru1Ajz1Yne4', 'fPRcLCvAzsI', 'duRZoanZZp4', 'o5nwU4lA47w', 'OV9HS0L_c9Q', 'isFb9eV_hQM', 'Hjam_4MhIQ0', '7Zb24Wwwt8Q', 'X8ok2s2Oxmc', '4oTkC5_KIxI', 'kCFOTs_ZNrE', 'ZEnYWZnn5uk', 'DhhLFo1Awjk', '7nfPBFOXlxo', 'zkqlo8x6hnk', '7oIRtQDl0wI', 'tf_np3pFTXo', 'BONXXHaLOWo', 'j69RCCVj7Xc', 'qYoNSKTWrws', 'UOTRXbV_vpM', '36GHmalMSIo', 'vWZhiJ7esc4', 'Qwyd2MEhjM0', 'RtRBPhB3o00', 'G0rL_GzQ79U', 'xLHo0QT2xtM', '1pv05hMOCBQ', 'mVxGmZzneA8', 'Og4wIo-PvNU', 'PL-0R5uecks', 'YN9Ie9aSCAo', 'YfsSOntNARs', 'guPWvE4nL5A', 'NJFUS4LlUmo', 'IT-clZ-R1yQ', 'xELLDbI0E5w', 'OTVmcBUC_Rg', 'UwIprPrEjsM', '6MdqTsnOyqE', 'HB6Ny189aZI', 'UH5oWs37rxI', 'qWJulrNfChE', '-VpaZ17YZfY', 'QWsNeg5YPGI', '0URIj0vVzbI', 'zi5jTF4TCVc', 'bC0CpqsniOQ', 'AYi-bFjW1fc', '_GhEkWXjM0c', 'vHrBB8QJm3Y', 'uy59ZC9ARH0', 'nX71d4qzvro', 'jdmDQ8j_PJU', 'ir5YZjJHRNU', 'dgkIOBlKXIg', 'd5IczwH0b9g', 'wisG9mY4qCg', 'yOgnnd3kf2k', '6XEf1tsb78c', 'c67sbJAJvL4', 'KQg3U-Acae4', 'si1TXRqEzmw', 'XUvZ4RKctiw', 'mIuotwdEbVE', 'QOHvhszJCb0', '55DINTLd6-A', 'bbvxEEaQVN8', 'C7t023DnwKE', 's-X74fxiq3A', '-rXZBzEBxKc', 'GEpOKH32SHU', 'jg8-H-H1DQ8', 'jR1Lb2LIw8U', 'tJLfpOZsd7w', 'nnnrM3clV10', 'v4D2DJq8HVQ', 'o6ZUMfqiyr4', 'q08iWBFwGI4', 'tj7PP2YbBPM', 'y9ySpO0ZWME', '7OJTKMnZDK4', 'ZgRuBs9HzG8', '4oqjtzNPtHU', 'FsDCDOS336k', 'AAMIRMflp8Q', 'ltrMF0HvcUo', '3Y8Kq-CTDw8', '3aRgseQI-_0', '5U_C4CF1RFM', 'tep8cL5kTdk', 'LS9jO08IWro', 'UVgN5CAGfR4', 'uRDUe9M2Ats', 'frJ4phulPRk', '-WzPvU3tnTE', '08wUzBQMF6k', 'LoZCY_PG0zc', 'opXJcrblgiU', 'sDQ_Q64ZtD4', '4iFm8kSCYT0', 'sW_CNNRuVoA', '_J01BTH2QGU', '1BbsD_xzII4', '42rhzC0DMg4', 'vz56zkrWpac', 'fiMXdV8qyHA', 'IRuZ-ZZbLvw', 'hsKze5IjX_Q', '2OiHY-wYnO4', 'nbthxql0IBQ', '3ojwueMRJNw', '9IOZ9_LHfyg', 'eHvz8ukZ0-A', 'k7QnbLzPchA', 'LQu0fbQFuu4', 'Quj5p93M-fQ', 'eQ2EASx1LtE', '7fR3tYLVRDo', 'iSG-KJ0h5gs', 'eC3nZAmOqsQ', '0MGv9ju2aaQ', 'cgB1LEoPbpQ', 'kq6bPSeYgFg', 'W4IvYeF-yT0', 'IAiem7UXkwQ', 'Dqt2hEqxbYs', 't8LndPnCg30', 'o93QLWjHr64', 'PBMdpbQtxHY', 'PDsY7jAUMAc', 'SYTCeReHDqY', 'Dr6bhWHvnw0', '9Sqf-YyBdAU', 'bKBYG0eTFiI', 'IIXxjU2rWpU', '5ESzRNzhVrA', 'aOmVL553sfo', 'lF4rdU-ZO_8', 'guwwEIEn4v0', 'c_R9G5XGkiE', 'eccuQFOkVtI', 'Jhr2myyK8J8', 'Na_gZadbgZQ', '9KM-BPhTRiM', 'JT6NKQ5HFlA', 'Tp220rBhBoM']

start=0
end=2
m=[]
while True:
    print(x[start:end])
    start=end
    end+=end



