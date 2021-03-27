def knee():

    import math

    # Physiological values.
    HAT_mass = 41.56
    HAT_MOI = 1.02
    HAT_length = 0.316
    thigh_mass = 6.1
    thigh_MOI = 0.116
    thigh_length = 0.43
    leg_mass = 9.8
    leg_MOI = 1.1
    leg_length = 0.9275
    body_mass = 61
    ecc = 0.06

    # Accelerations and dynamics
    thigh_X = 2.6
    thigh_Y = 17
    thigh_alpha = -1.396
    trunk_X = 0.9112
    trunk_Y = 21.17
    trunk_alpha = -2.853
    otherleg_X = 2.606
    otherleg_Y = 15.15
    otherleg_alpha = -1.396
    g = 9.81

    # Defining some constants
    deg_49 = 49 * math.pi / 180
    deg_53 = 53 * math.pi / 180
    deg_62 = 62 * math.pi / 180
    deg_40 = 40 * math.pi / 180

    # Head-ankle-trunk calculations
    F_xHhat = HAT_mass * trunk_X
    F_yHhat = HAT_mass * (g + trunk_Y)
    M_Hhat = HAT_MOI * trunk_alpha - F_xHhat * math.sin(deg_49) * 0.32 + F_yHhat * math.cos(deg_49) * 0.32

    # Non-landing leg values
    F_xHll = leg_mass * otherleg_X
    F_yHll = leg_mass * (g + otherleg_Y)
    M_Hll = leg_MOI * otherleg_alpha + F_xHll * math.sin(deg_53) * 0.35 + F_yHll * math.cos(deg_53) * 0.35

    # Finding values at the hip
    F_xH = F_xHhat + F_xHll
    F_yH = F_yHhat + F_yHll
    M_H = M_Hhat + M_Hll

    # Finding values at the knee
    F_xK = thigh_mass * thigh_X - F_xH
    F_yK = thigh_mass * thigh_Y - F_yH + thigh_mass * g
    M_K = thigh_MOI * thigh_alpha + F_xH * math.sin(deg_62) * 0.19 + F_yH * math.sin(deg_62) * 0.19 - M_H - F_xK * math.sin(deg_62) * 0.24 - F_yK * math.cos(deg_62) * 0.24

    # Displaying data
    print(F_xH,F_yH,M_H)
    print(F_xK,F_yK,M_K)
    print(F_xH/(g*body_mass),F_yH/(g*body_mass),M_H/(g*body_mass))
    print(F_xK/(g*body_mass),F_yK/(g*body_mass),M_K/(g*body_mass))

    # Converting intersegmental data to bone-on-bone and muscle forces
    F_M = M_K/ecc
    F_by = F_yK - math.cos(deg_40) * F_M
    F_bx = F_xK - math.sin(deg_40) * F_M
    F_btot = (F_by ** 2 + F_bx ** 2) ** 0.5

    # Displaying data
    print(F_M,F_btot, F_bx, F_by)
    print(F_M/(g*body_mass),F_btot/(g*body_mass),F_bx/(g*body_mass),F_by/(g*body_mass))

knee()