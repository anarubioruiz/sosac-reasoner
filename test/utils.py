from clorm import monkey
monkey.patch() # must call this before importing clingo
from clingo import Control

import terms


class ClingoTest:
    def clingo_setup(self, *files):
        self.ctrl = Control(unifier=[
            terms.Device,

            terms.locatedAt,
            terms.klassObservesProperty,
            terms.makesObservationKlass,
            terms.klassActsOnProperty,
            terms.makesActuationKlass,

            # CLINGO TERMS ---------

            terms.Sensor,
            terms.ObservableProperty,
            terms.Observation,
            terms.Act,
            terms.Actuator,
            terms.Actuation,
            terms.ActuatableProperty,
            terms.FeatureOfInterest,
            terms.Result,
            terms.Platform,

            terms.isObservedBy,
            terms.observes,
            terms.makesObservation,
            terms.madeBySensor,
            terms.observedProperty,
            terms.makesActuation,
            terms.isActedOnBy,
            terms.madeByActuator,
            terms.actsOnProperty,
            terms.hasFeatureOfInterest,
            terms.isFeatureOfInterestOf,
            terms.hasResult,
            terms.isResultOf,
            terms.hasSimpleResult,
            terms.hosts,
            terms.isHostedBy,
            terms.hasProperty
        ])

        if not files:
            self.ctrl.load("src/engine.lp")
            self.ctrl.load("src/sosa_engine.lp")
            return

        for f in files:
            self.ctrl.load(f)


    def load_knowledge(self, facts):
        self.ctrl.add_facts(facts)
        self.ctrl.ground([("base", [])])

    def get_solution(self):
        solution = None

        def on_model(model):
            nonlocal solution
            solution = model.facts(atoms=True)
            print(solution)

        self.ctrl.solve(on_model=on_model)
        return solution
