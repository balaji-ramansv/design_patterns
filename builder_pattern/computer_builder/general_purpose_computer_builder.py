from computer_builder import ComputerBuilder

class GeneralPurposeComputerBuilder(ComputerBuilder):
    @classmethod
    def build(cls):
        gpc_builder = ComputerBuilder(computer_type="General Purpose")
        final_computer = gpc_builder.build_cpu("8 cores").build_ram("16 GB").build_storage("1 TB").build_graphic_card("4 cores").build_os("Ubuntu").build()
        print(final_computer)
