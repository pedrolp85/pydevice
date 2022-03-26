import ipaddress
import os
from typing import Optional

from fetchdata import get_fetchdata
from scheduler import get_task_scheduler

import typer

app = typer.Typer()


@app.command()
def task_scheduler(
    device: int = typer.Option(None, "--device", "-d", help="Get devices from Backend"),
    manufacturer: int = typer.Option(None, "--manufacturer", "-m", help="Get Manufacturers from Backend"),
    interface: int = typer.Option(None, "--interface", "-i", help="Get Interfaces from Backend")    
) -> None:

    data = get_fetchdata()
    
    if device: 
        print (data.get_devices())

    schel = get_task_scheduler()
    msg = schel.send_test_msg()
    msg_rcv = schel.recv_test_msg()


if __name__ == "__main__":
    app()
