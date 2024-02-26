from Functions import *
def func(functionName):
    functionName = functionName.lower()
    if functionName == 'ACKLEY'.lower():
        return lambda x:ACKLEY(x)
    elif functionName == 'BUKIN'.lower():
        return lambda x:BUKIN(x)
    elif functionName == 'CROSS_IN_TRAY'.lower():
        return lambda x:CROSS_IN_TRAY(x)
    elif functionName == 'DROP_WAVE'.lower():
        return lambda x:DROP_WAVE(x)
    elif functionName == 'EGGHOLDER'.lower():
        return lambda x:EGGHOLDER(x)
    elif functionName == 'GRIEWANK'.lower():
        return lambda x:GRIEWANK(x)
    elif functionName == 'HOLDER_TABLE'.lower():
        return lambda x:HOLDER_TABLE(x)
    elif functionName == 'Langermann'.lower():
        return lambda x:Langermann(x)
    elif functionName == 'Levy'.lower():
        return lambda x:Levy(x)
    elif functionName == 'Rastrigin'.lower():
        return lambda x:Rastrigin(x)
    elif functionName == 'schaffer2'.lower():
        return lambda x:schaffer2(x)
    elif functionName == 'schaffer4'.lower():
        return lambda x:schaffer4(x)
    elif functionName == 'Schwefel'.lower():
        return lambda x:Schwefel(x)
    elif functionName == 'Shubert'.lower():
        return lambda x:Shubert(x)
    elif functionName == 'Bohachevsky'.lower():
        return lambda x:Bohachevsky(x)
    elif functionName == 'Perm'.lower():
        return lambda x:Perm(x)
    elif functionName == 'Rotated_Hyper_Ellipsoid'.lower():
        return lambda x:Rotated_Hyper_Ellipsoid(x)
    elif functionName == 'spheref'.lower():
        return lambda x:spheref(x)
    elif functionName == 'sumpow'.lower():
        return lambda x:sumpow(x)
    elif functionName == 'sumsqu'.lower():
        return lambda x:sumsqu(x)
    elif functionName == 'trid'.lower():
        return lambda x:trid(x)
    elif functionName == 'booth'.lower():
        return lambda x:booth(x)
    elif functionName == 'matya'.lower():
        return lambda x:matya(x)
    elif functionName == 'mccorm'.lower():
        return lambda x:mccorm(x)
    elif functionName == 'powersum'.lower():
        return lambda x:powersum(x)
    elif functionName == 'zakharov'.lower():
        return lambda x:zakharov(x)
    elif functionName == 'camel3'.lower():
        return lambda x:camel3(x)
    elif functionName == 'camel6'.lower():
        return lambda x:camel6(x)
    elif functionName == 'dixonpr'.lower():
        return lambda x:dixonpr(x)
    elif functionName == 'rosen'.lower():
        return lambda x:rosen(x)
    elif functionName == 'dejong5'.lower():
        return lambda x:dejong5(x)
    elif functionName == 'easom'.lower():
        return lambda x:easom(x)
    elif functionName == 'michal'.lower():
        return lambda x:michal(x)
    elif functionName == "Bent_Cigar".lower():
        return lambda x:x[0]**2 + 10**6 * sum([x[i] for i in range(len(x)) if i != 0])
    elif functionName == "Modified_Schwefel".lower():
        return lambda x: 418.9829 * len(x) - sum([Modified_Schwefel_g(i, x) for i in x])
    # Constrained optimization problems
    elif functionName == 'RosenbrockConstrained':
        return lambda x:RosenbrockConstrained1(x)
    elif functionName == 'RosenbrockConstrained2':
        return lambda x:RosenbrockConstrained2(x)
    elif functionName == 'Mishras_Bird':
        return lambda x:Mishras_Bird(x)
    elif functionName == 'Townsend'.lower():
        return lambda x:Townsend(x)
    elif functionName == 'Gomez_and_Levy'.lower():
        return lambda x:Gomez_and_Levy(x)
    elif functionName == 'Simionescu'.lower():
        return lambda x:Simionescu(x)
    elif functionName == 'bent_cigar_function':
        return lambda x:bent_cigar_function(x)
    elif functionName == 'Discus'.lower():
        return lambda x:Discus(x)
    elif functionName == 'six_hump'.lower():
        return lambda x:six_hump(x)


def Modified_Schwefel_g(i, x):
    d = len(x)
    zz = i + 4.209687462275036e+002
    if np.abs(zz) <= 500:
        return zz * np.sin(np.sqrt(np.abs(zz)))
    elif zz > 500:
        return (500 - (zz % 500)) * np.sin(np.sqrt(np.abs(500 - (zz % 500)))) - (zz - 500)**2/(10000 * d)
    elif zz < -500:
        return ((np.abs(zz)%500) - 500) * np.sin(np.sqrt(np.abs(zz)%500 - 500)) - (zz + 500)**2/(10000 * d)

def plotfunc3d(testFunctions, lb = -5, ub=5):    
    n = 1    
    Nrows = int(np.ceil(len(testFunctions) / 3))    
    fig = plt.figure(figsize=(10, 40))
    for k in range(testFunctions.shape[0]):        
        functionName = testFunctions.iloc[k, 0]
        fn = func(functionName)
        x = np.linspace(lb, ub, 400)
        y = np.linspace(lb, ub, 400)
        X, Y = np.meshgrid(x, y)    
        Z = np.array([fn([X[i, j], Y[i, j]]) for i in range(X.shape[0]) for j in range(X.shape[1])]).reshape(400, 400)
        ax = fig.add_subplot(Nrows, 3, n, projection='3d')
        ax.plot_surface(X, Y, Z, cmap = 'jet')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('f(x)')
        ax.set_title(functionName)
        n += 1
    plt.tight_layout()

def plotfunccontour(testFunctions, lb = -5, ub=5):    
    n = 1    
    Nrows = int(np.ceil(len(testFunctions) / 3))    
    fig = plt.figure(figsize=(10, 40))
    for k in range(testFunctions.shape[0]):        
        functionName = testFunctions.iloc[k, 0]
        fn = func(functionName)
        x = np.linspace(lb, ub, 400)
        y = np.linspace(lb, ub, 400)
        X, Y = np.meshgrid(x, y)    
        Z = np.array([fn([X[i, j], Y[i, j]]) for i in range(X.shape[0]) for j in range(X.shape[1])]).reshape(400, 400)
        ax = fig.add_subplot(Nrows, 3, n)
        ax.contourf(X, Y, Z, levels = 50,  cmap = 'jet')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')        
        ax.set_title(functionName)
        n += 1
    plt.tight_layout()         