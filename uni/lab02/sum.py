#
#
#


def simpleSum(par1, par2, optPar=34):
    return par1 + par2 + optPar

print(simpleSum(12, 3))


def keywordsArgFunc(par1=0, par2=0, par3=0):
    return par1 * par2 * par3


print(keywordsArgFunc(par1=2, par2=2, par3=1))