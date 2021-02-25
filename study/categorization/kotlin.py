from bug import KotlinBug
import categories as ct
import characteristics as pc
import symptoms as sy
import root_causes as rc


kotlin_iter1 = [
    KotlinBug(
        "1.KT-1934",
        [pc.Inheritance()],
        False,
        sy.Runtime(sy.WrongMethodCalled()),
        rc.MissingCase(),
        ct.Declarations(), # -- During Override Resolution
        4
    ),
    KotlinBug(
        "2.KT-4814",
        [pc.ArithmeticExpressions()],
        False,
        sy.Runtime(sy.VerifyError()),
        rc.MissingCase(),
        ct.TypeExpression(),
        4
    ),
    KotlinBug(
        "3.KT-42175",
        [
            pc.Lambdas(),
            pc.Collections(),
            pc.This()
        ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Inference(),  # "type variable substitution"
        8
    ),
    KotlinBug(
        "4.KT-10244",
        [pc.FlowTyping(),
         pc.IntersectionTypes(), # -- Implicit -- Inferred, should we keep it?
         pc.Conditionals()],
        False,
        sy.InternalCompilerError(),
        rc.MissingCase(), # Design issue -- InsufficientFunctionality -- MissingCase, all makes sense to me
        ct.Declarations(), # -- During Decleration Checker
        4
    ),
    KotlinBug(
        "5.KT-10472",
        [pc.Overloading(), pc.Varargs(), 
         pc.ParameterizedClasses(),
         pc.ParameterizedFunctions(),
         pc.ParameterizedTypes()], # -- Do we really need to keep track of Parameterized Types?
        True,
        sy.Runtime(sy.NullPointerException()),
        rc.MissingCase(), # IncorrectSequence, definitely not a missing case but some other logic error 
        ct.Resolution(),
        8
    ),
    KotlinBug(
        "6.KT-7485",
        [pc.Where(),
         pc.BoundedPolymorphism(),
         pc.ParameterizedFunctions(),
         pc.ParameterizedClasses(),
         pc.Nullables(),
         pc.Subtyping()],
        False,
        sy.Runtime(sy.NullPointerException()),
        rc.IncorrectComputation(), # IncorrectCondition
        ct.SubtypingRelated(), # Declarations -- Similar to KT-10244
        11
    ),
    KotlinBug(
        "7.KT-23748",
        [pc.ParameterizedFunctions(),
         pc.Subtyping(),
         pc.Nullables(),
         pc.ElvisOperator()],
        True,
        sy.CompileTimeError(),
        # This is not a Design Issue but something is going wrong with elvis operator
        # and exact Annotation, it could be a logic error or an algorithmic error.
        # I propose to remove this bug because we don't have the fix for it.
        rc.DesignIssue(), 
        ct.Inference(),  # constraint solving
        9
    ),
    KotlinBug(
        "8.KT-22728",
        [pc.Lambdas(),
         pc.ExtensionFunctions(),
         pc.Typedefs(),
         pc.Import(), # -- It means multiple packages?
         pc.FunctionTypes()],
        True,
        sy.CompileTimeError(),
        rc.WrongParams(),
        ct.Mechanics(), # -- serialization
        11
    ),
    KotlinBug(
        "9.KT-10711",
        # FunctionTypes?
        # Remove Collections?
        [pc.ParameterizedFunctions(),
         pc.Collections(),
         pc.FunctionReferences()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(), # InsufficientFunctionality or IncorrectSequence
        ct.Inference(),  # constraint solving
        6
    ),
    KotlinBug(
        "10.KT-37249",
        [pc.Conditionals(), pc.TryCatch(), pc.Lambdas()],
        True,
        sy.CompileTimeError(),
        rc.InsufficientFunctionality(),
        ct.Inference(),  # constraint solving
        7
    ),
    KotlinBug(
        "11.KT-11468",
        [pc.ParameterizedClasses(), pc.DeclVariance(),
         pc.ParameterizedTypes(),
         pc.Subtyping()],
        True,
        sy.InternalCompilerError(),
        rc.DesignIssue(),
        ct.SubtypingRelated(), # Why not Decleration? Maybe TypeApproximation?
        6
    ),
    KotlinBug(
        "12.KT-6014",
        [pc.Overriding(), pc.Inheritance(), pc.Delegation()],
        True,
        sy.CompileTimeError(),
        rc.IncorrectComputation(),
        ct.Resolution(),
        7
    ),
    KotlinBug(
        "13.KT-12044",
        # Pair -> Collections? otherwise Generic with properties?
        [pc.Conditionals(), pc.PropertyReference()],
        True,
        sy.CompileTimeError(),
        rc.WrongParams(),
        ct.Resolution(),
        8
    ),
    KotlinBug(
        "14.KT-4334",
        [pc.Lambdas(), pc.Loops()],
        False,
        sy.InternalCompilerError(),
        rc.MissingCase(),
        ct.OtherSemanticChecking(), # -- BREAK_OR_CONTINUE_JUMPS_ACROSS_FUNCTION_BOUNDARY
        7
    ),
    KotlinBug(
        "15.KT-32184",
        # FunctionType?
        [pc.Lambdas(), pc.DataClasses()],
        True,
        sy.InternalCompilerError(),
        rc.WrongParams(),
        ct.Resolution(), 
        12
    ),
    KotlinBug(
        "16.KT-10197",
        [pc.Overriding(), pc.Inheritance(), pc.Delegation()],
        False,
        sy.Runtime(sy.AbstractMethodError()),
        rc.MissingCase(), # InsufficientFunctionality
        ct.Declarations(), # -- During Override Resolution
        12
    ),
    KotlinBug(
        "17.KT-41693",
        [pc.Conditionals(), pc.Import(),
         pc.FlexibleTypes(), # Java Types are loaded as flexible types
         pc.JavaInterop()],
        True,
        sy.Runtime(sy.NullPointerException()),
        rc.MissingCase(), # IncorrectComputation
        ct.Approximation(),
        16
    ),
    KotlinBug(
        "18.KT-44420",
        [pc.FlexibleTypes(), 
         pc.Collections(),
         pc.VarTypeInference(),
         pc.JavaInterop()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(), #InsufficientFunctionality
        ct.Approximation(),
        9
    ),
    KotlinBug(
        "19.KT-35602",
        [pc.ParameterizedClasses(),
         pc.FBounded(),
         pc.ParameterizedTypes(),
         pc.UseVariance(),
         pc.NullAssertion()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Approximation(),
        6
    ),
    KotlinBug(
        "20.KT-6992",
        [pc.Overloading(),
         pc.ParameterizedClasses(),
         pc.Delegation(), # ?
         pc.This()],
        False,
        sy.MisleadingReport(),
        rc.MissingCase(), #InsufficientFunctionality
        ct.Resolution()
    ),
    3
]


kotlin_iter2 = [
    KotlinBug(
        "1.KT-31102",
        [pc.Lambdas(), pc.FunctionReferences(),
         pc.ParameterizedFunctions()],
        True,
        sy.CompileTimeError(),
        rc.InsufficientFunctionality(),
        ct.Inference()  # constraint solving
    ),
    KotlinBug(
        "2.KT-3112",
        [pc.NestedDeclaration(),
         pc.ParameterizedClasses(),
         pc.TypeArgsInference()],
        False,
        sy.MisleadingReport(),
        rc.InsufficientFunctionality(),
        ct.Inference()
    ),
    KotlinBug(
        "3.KT-11721",
        [pc.Overriding()],
        False,
        sy.MisleadingReport(),
        rc.IncorrectCondition(),
        ct.Resolution()  # Misc
    ),
    KotlinBug(
        "4.KT-39461",
        [pc.Coroutines(), pc.OperatorOverloading(),
         pc.Lambdas(),
         pc.ParameterizedFunctions(),
         pc.FunctionTypes()
         ],
        True,
        sy.CompileTimeError(),
        rc.IncorrectComputation(),
        ct.Resolution()
    ),
    KotlinBug(
        "5.KT-15226",
        [pc.JavaInterop(),
         pc.Overriding(),
         pc.Delegation()],
        True,
        sy.Runtime(sy.WrongMethodCalled()),
        rc.DesignIssue(),
        ct.Declarations(),
    ),
    KotlinBug(
        "6.KT-6720",
        [pc.Overriding(),
         pc.JavaInterop()],
        False,
        sy.Runtime(sy.AbstractMethodError()),
        rc.IncorrectComputation(),
        ct.Resolution()
    ),
    KotlinBug(
        "7.KT-37644",
        [pc.ElvisOperator(),
         pc.Collections(),
         pc.ParameterizedTypes()
         ],
        True,
        sy.InternalCompilerError(),
        rc.ExtraneousComputation(),
        ct.Inference(),  # contraint solving
    ),
    KotlinBug(
        "8.KT-18129",
        [pc.Reflection(),
         pc.OperatorOverloading(),
         pc.Delegation(),
         pc.ParameterizedTypes(),
         pc.Nullables(),
         pc.FlowTyping()],
        False,
        sy.Runtime(sy.NullPointerException()),
        rc.DesignIssue(),
        ct.Environment(),  # XXX
    ),
    KotlinBug(
        "9.KT-18522",
        [pc.Conditionals(), pc.Import(),
         pc.ParameterizedClasses(),
         pc.ParameterizedTypes()
         ],
        False,
        sy.InternalCompilerError(),
        rc.IncorrectCondition(),  # Wrong loop iteration
        ct.SubtypingRelated()
    ),
    KotlinBug(
        "10.KT-8320",
        [pc.ParameterizedFunctions(),
         pc.TryCatch()],
        False,
        sy.Runtime(sy.ClassCastException()),
        rc.MissingCase(),
        ct.Declarations()
    ),
    KotlinBug(
        "11.KT-32081",
        [pc.ParameterizedClasses(),
         pc.ParameterizedFunctions(),
         pc.ParameterizedTypes(),
         pc.Conditionals(),
         pc.AnonymousClass(),
         pc.Nothing(),
         pc.Subtyping(),
         pc.This(),
         pc.DataClasses(),
         pc.OperatorOverloading(),
         pc.ExtensionFunctions()],
        True,
        sy.CompileTimeError(),
        rc.WrongParams(),
        ct.Inference()  # constraint solving
    ),
    KotlinBug(
        "12.KT-11280",
        [pc.Overriding(),
         pc.Subtyping(),
         pc.FlowTyping()],
        False,
        sy.Runtime(sy.RuntimeSymptom()),
        rc.DesignIssue(),
        ct.Environment()  # XXX
    ),
    KotlinBug(
        "13.KT-42825",
        [pc.Conditionals(),
         pc.ParameterizedClasses(),
         pc.UseVariance(),
         pc.FlexibleTypes(), pc.Nullables(),
         pc.JavaInterop(),
         pc.FlowTyping()],
        True,
        sy.CompileTimeError(),
        rc.WrongParams(),
        ct.SubtypingRelated()
    ),
    KotlinBug(
        "14.KT-17597",
        [pc.Collections(), pc.AccessModifiers(),
         pc.StaticMethod(),
         pc.JavaInterop(),
         pc.FunctionReferences()],
        True,
        sy.CompileTimeError(),
        rc.IncorrectCondition(),
        ct.Resolution(),
    ),
    KotlinBug(
        "15.KT-13597",
        [pc.AnonymousClass()],
        False,  # change final field
        sy.Runtime(sy.IllegalAccessError()),
        rc.InsufficientFunctionality(),
        ct.OtherSemanticChecking(),
    ),
    KotlinBug(
        "16.KT-12738",
        [pc.ParameterizedFunctions(),
         pc.FunctionReferences()],
        True,
        sy.CompileTimeError(),
        rc.InsufficientFunctionality(),
        ct.Resolution()
    ),
    KotlinBug(
        "17.KT-37628",
        [pc.Collections(),
         pc.Conditionals(),
         pc.Nullables(),
         pc.Subtyping(),
         pc.Lambdas()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Inference(),  # constraint solving
    ),
    KotlinBug(
        "18.KT-12286",
        [pc.ParameterizedFunctions(),
         pc.FBounded(),
         pc.Conditionals(),
         pc.FunctionReferences()],
        True,
        sy.CompileTimeError(),
        rc.InsufficientFunctionality(),
        ct.Inference(),  # constraint solving
    ),
    KotlinBug(
        "19.KT-9630",
        [pc.ParameterizedClasses(),
         pc.Inheritance(),
         pc.ParameterizedFunctions(),
         pc.ParameterizedTypes(),
         pc.FBounded(),
         pc.Where(),
         pc.IntersectionTypes(),
         pc.ExtensionFunctions()],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Approximation()
    ),
    KotlinBug(
        "20.KT-25302",
        [pc.ParameterizedFunctions(),
         pc.ParameterizedClasses(),
         pc.UseVariance(),
         pc.ParameterizedTypes(),
         ],
        True,
        sy.CompileTimeError(),
        rc.MissingCase(),
        ct.Inference()  # constraint solving
    )
]
