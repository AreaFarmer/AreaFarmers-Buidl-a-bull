from pyteal import *

from AreaFarmers_contract import Product

if __name__ == "__main__":
    approval_program = Product().approval_program()
    clear_program = Product().clear_program()

    # Mode.Application specifies that this is a smart contract
    compiled_approval = compileTeal(approval_program, Mode.Application, version=6)
    print(compiled_approval)
    with open("AreaFarmers_approval.teal", "w") as teal:
        teal.write(compiled_approval)
        teal.close()

    # Mode.Application specifies that this is a smart contract
    compiled_clear = compileTeal(clear_program, Mode.Application, version=6)
    print(compiled_clear)
    with open("AreaFarmers_clear.teal", "w") as teal:
        teal.write(compiled_clear)
        teal.close()