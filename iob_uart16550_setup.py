#!/usr/bin/env python3

import os, sys

sys.path.insert(0, os.getcwd() + "/submodules/LIB/scripts")
import setup

name = "iob_uart16550"
version = "V0.10"
flows = "sim emb"
if setup.is_top_module(sys.modules[__name__]):
    setup_dir = os.path.dirname(__file__)
    build_dir = f"../{name}_{version}"
submodules = {
    "hw_setup": {"headers": ["iob_s_port", "iob_s_portmap", "iob_wire"], "modules": []},
}

confs = [
    # Macros
    # Parameters
    # IOb-bus Parameters
    {
        "name": "DATA_W",
        "type": "P",
        "val": "32",
        "min": "NA",
        "max": "NA",
        "descr": "Data bus width",
    },
    {
        "name": "ADDR_W",
        "type": "P",
        "val": "16",
        "min": "NA",
        "max": "NA",
        "descr": "Address bus width",
    },
]

ios = [
    {"name": "iob_s_port", "descr": "CPU native interface", "ports": []},
    {
        "name": "general",
        "descr": "GENERAL INTERFACE SIGNALS",
        "ports": [
            {
                "name": "clk_i",
                "type": "I",
                "n_bits": "1",
                "descr": "System clock input",
            },
            {
                "name": "arst_i",
                "type": "I",
                "n_bits": "1",
                "descr": "System reset, asynchronous and active high",
            },
            {
                "name": "cke_i",
                "type": "I",
                "n_bits": "1",
                "descr": "System reset, asynchronous and active high",
            },
        ],
    },
    {
        "name": "rs232",
        "descr": "UART16550 rs232 interface signals.",
        "ports": [
            # {'name':'interrupt', 'type':'O', 'n_bits':'1', 'descr':'be done'},
            {
                "name": "txd",
                "type": "O",
                "n_bits": "1",
                "descr": "Serial transmit line",
            },
            {"name": "rxd", "type": "I", "n_bits": "1", "descr": "Serial receive line"},
            {
                "name": "cts",
                "type": "I",
                "n_bits": "1",
                "descr": "Clear to send; the destination is ready to receive a transmission sent by the UART",
            },
            {
                "name": "rts",
                "type": "O",
                "n_bits": "1",
                "descr": "Ready to send; the UART is ready to receive a transmission from the sender",
            },
        ],
    },
    {
        "name": "interrupt",
        "descr": "UART16550 interrupt related signals",
        "ports": [
            {
                "name": "interrupt",
                "type": "O",
                "n_bits": "1",
                "descr": "UART interrupt source",
            },
        ],
    },
]

regs = []
blocks = []


# Main function to setup this core and its components
def main():
    setup.setup(sys.modules[__name__])


if __name__ == "__main__":
    main()
