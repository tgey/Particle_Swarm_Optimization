import functions.activitions as act
configs = [
    #Choice activations functions
    #{ "shape": [3, 3, 1], "activations": [act.Sigmoid, act.Sigmoid, act.Tanh], "nb_particles": 20, "max_iter": 15, "inertia_cst": 0.9, "cognative_cst": 1.4960, "social_cst": 1.4960, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Relu, act.Relu, act.Tanh], "nb_particles": 20, "max_iter": 15, "inertia_cst": 0.9, "cognative_cst": 1.4960, "social_cst": 1.4960, "bounds": [-2.0, 2.0]}, # TODO reference https://www.hindawi.com/journals/cin/2015/369298/
    #{ "shape": [3, 3, 1], "activations": [act.Relu, act.Relu, act.Sigmoid], "nb_particles": 20, "max_iter": 15, "inertia_cst": 0.9, "cognative_cst": 1.4960, "social_cst": 1.4960, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Sigmoid], "nb_particles": 20, "max_iter": 15, "inertia_cst": 0.9, "cognative_cst": 1.4960, "social_cst": 1.4960, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 10, "max_iter": 10, "inertia_cst": 0.5, "cognative_cst": 1.4960, "social_cst": 1.4960, "bounds": [-2.0, 2.0]},

    #Number of hidden layers and hidden neurons
    #{ "shape": [1, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 10, "max_iter": 10, "inertia_cst": 0.5, "cognative_cst": 1.4960, "social_cst": 1.4960, "bounds": [-2.0, 2.0]},
    #{ "shape": [5, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 10, "max_iter": 10, "inertia_cst": 0.5, "cognative_cst": 1.4960, "social_cst": 1.4960, "bounds": [-2.0, 2.0]},
    #{ "shape": [10, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 10, "max_iter": 10, "inertia_cst": 0.5, "cognative_cst": 1.4960, "social_cst": 1.4960, "bounds": [-2.0, 2.0]},
    #{ "shape": [2, 1, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 10, "max_iter": 10, "inertia_cst": 0.5, "cognative_cst": 1.4960, "social_cst": 1.4960, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 10, "max_iter": 10, "inertia_cst": 0.5, "cognative_cst": 1.4960, "social_cst": 1.4960, "bounds": [-2.0, 2.0]},
    #{ "shape": [10, 10, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 10, "max_iter": 10, "inertia_cst": 0.5, "cognative_cst": 1.4960, "social_cst": 1.4960, "bounds": [-2.0, 2.0]},

    #Constante
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1, "social_cst": 1, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.2, "social_cst": 1, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.2, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.2, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.2, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.2, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.2, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.4, "social_cst": 1, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.4, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.4, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.4, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.4, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.4, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.6, "social_cst": 1, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.6, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.6, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.6, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.6, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.6, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.8, "social_cst": 1, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.8, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.8, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.8, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.8, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 1.8, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 2, "social_cst": 1, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 2, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 2, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 2, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 2, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.2, "cognative_cst": 2, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1, "social_cst": 1, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.2, "social_cst": 1, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.2, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.2, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.2, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.2, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.2, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.4, "social_cst": 1, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.4, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.4, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.4, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.4, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.4, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.6, "social_cst": 1, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.6, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.6, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.6, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.6, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.6, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.8, "social_cst": 1, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.8, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.8, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.8, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.8, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 1.8, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 2, "social_cst": 1, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 2, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 2, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 2, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 2, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.4, "cognative_cst": 2, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1, "social_cst": 1, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.2, "social_cst": 1, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.2, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.2, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.2, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.2, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.2, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.4, "social_cst": 1, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.4, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.4, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.4, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.4, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.4, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.6, "social_cst": 1, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.6, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.6, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.6, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.6, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.6, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.8, "social_cst": 1, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.8, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.8, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.8, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.8, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 1.8, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 2, "social_cst": 1, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 2, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 2, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 2, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 2, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.6, "cognative_cst": 2, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1, "social_cst": 1, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.2, "social_cst": 1, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.2, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.2, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.2, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.2, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.2, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.4, "social_cst": 1, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.4, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.4, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.4, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.4, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.4, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.6, "social_cst": 1, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.6, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.6, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.6, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.6, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.6, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.8, "social_cst": 1, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.8, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.8, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.8, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.8, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.8, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 2, "social_cst": 1.2, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 2, "social_cst": 1.4, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 2, "social_cst": 1.6, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 2, "social_cst": 1.8, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 30, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 2, "social_cst": 2, "bounds": [-2.0, 2.0]},

    #Numbers of particles
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 20, "max_iter": 1, "inertia_cst": 0.8, "cognative_cst": 1.495, "social_cst": 1.495, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 20, "max_iter": 25, "inertia_cst": 0.8, "cognative_cst": 1.495, "social_cst": 1.495, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 20, "max_iter": 50, "inertia_cst": 0.8, "cognative_cst": 1.495, "social_cst": 1.495, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 20, "max_iter": 100, "inertia_cst": 0.8, "cognative_cst": 1.495, "social_cst": 1.495, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 20, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.495, "social_cst": 1.495, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 20, "max_iter": 200, "inertia_cst": 0.8, "cognative_cst": 1.495, "social_cst": 1.495, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 20, "max_iter": 250, "inertia_cst": 0.8, "cognative_cst": 1.495, "social_cst": 1.495, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 50, "max_iter": 1, "inertia_cst": 0.8, "cognative_cst": 1.495, "social_cst": 1.495, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 50, "max_iter": 25, "inertia_cst": 0.8, "cognative_cst": 1.495, "social_cst": 1.495, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 50, "max_iter": 50, "inertia_cst": 0.8, "cognative_cst": 1.495, "social_cst": 1.495, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 50, "max_iter": 100, "inertia_cst": 0.8, "cognative_cst": 1.495, "social_cst": 1.495, "bounds": [-2.0, 2.0]},
    #{ "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 50, "max_iter": 150, "inertia_cst": 0.8, "cognative_cst": 1.495, "social_cst": 1.495, "bounds": [-2.0, 2.0]},
    { "shape": [3, 3, 1], "activations": [act.Tanh, act.Tanh, act.Tanh], "nb_particles": 50, "max_iter": 200, "inertia_cst": 0.8, "cognative_cst": 1.495, "social_cst": 1.495, "bounds": [-2.0, 2.0]},

]
