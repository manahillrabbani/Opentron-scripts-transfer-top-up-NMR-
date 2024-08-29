from pprint import pprint
from opentrons import protocol_api
import json
from pathlib import Path
from collections import defaultdict
from opentrons.types import Point

# metadata
metadata = {
    "protocolName": "MS_transfer_upto_F8",
    "author": "Steven Bennett<s.bennett18@imperial.ac.uk>, Annabel Basford <a.basford20@imperial.ac.uk>",
    "description": "High-Throughput Run Tranfer 20uL for MS",
    "apiLevel": "2.9",
}

substance_locations = {
    "3": {
        "name": "Stock",
        "type": "analyticalsales_48_wellplate_2000ul",
        "A1": {
            "substance": "A1",
            "amount": 700
        },
        "A2": {
            "substance": "A2",
            "amount": 700
        },
        "A3": {
            "substance": "A3",
            "amount": 700
        },
        "A4": {
            "substance": "A4",
            "amount": 700
        },
        "A5": {
            "substance": "A5",
            "amount": 700
        },
        "A6": {
            "substance": "A6",
            "amount": 700
        },
        "A7": {
            "substance": "A7",
            "amount": 700
        },
        "A8": {
            "substance": "A8",
            "amount": 700
        },
        "B1": {
            "substance": "B1",
            "amount": 700
        },
        "B2": {
            "substance": "B2",
            "amount": 700
        },
        "B3": {
            "substance": "B3",
            "amount": 700
        },
        "B4": {
            "substance": "B4",
            "amount": 700
        },
        "B5": {
            "substance": "B5",
            "amount": 700
        },
        "B6": {
            "substance": "B6",
            "amount": 700
        },
        "B7": {
            "substance": "B7",
            "amount": 700
        },
        "B8": {
            "substance": "B8",
            "amount": 700
        },
        "C1": {
            "substance": "C1",
            "amount": 700
        },
        "C2": {
            "substance": "C2",
            "amount": 700
        },
        "C3": {
            "substance": "C3",
            "amount": 700
        },
        "C4": {
            "substance": "C4",
            "amount": 700
        },
        "C5": {
            "substance": "C5",
            "amount": 700
        },
        "C6": {
            "substance": "C6",
            "amount": 700
        },
        "C7": {
            "substance": "C7",
            "amount": 700
        },
        "C8": {
            "substance": "C8",
            "amount": 700
        },
        "D1": {
            "substance": "D1",
            "amount": 700
        },
        "D2": {
            "substance": "D2",
            "amount": 700
        },
        "D3": {
            "substance": "D3",
            "amount": 700
        },
        "D4": {
            "substance": "D4",
            "amount": 700
        },
        "D5": {
            "substance": "D5",
            "amount": 700
        },
        "D6": {
            "substance": "D6",
            "amount": 700
        },
        "D7": {
            "substance": "D7",
            "amount": 700
        },
        "D8": {
            "substance": "D8",
            "amount": 700
        },
        "E1": {
            "substance": "E1",
            "amount": 700
        },
        "E2": {
            "substance": "E2",
            "amount": 700
        },
        "E3": {
            "substance": "E3",
            "amount": 700
        },
        "E4": {
            "substance": "E4",
            "amount": 700
        },
        "E5": {
            "substance": "E5",
            "amount": 700
        },
        "E6": {
            "substance": "E6",
            "amount": 700
        },
        "E7": {
            "substance": "E7",
            "amount": 700
        },
        "E8": {
            "substance": "E8",
            "amount": 700
        },
        "F1": {
            "substance": "F1",
            "amount": 700
        },
        "F2": {
            "substance": "F2",
            "amount": 700
        },
        "F3": {
            "substance": "F3",
            "amount": 700
        },
        "F4": {
            "substance": "F4",
            "amount": 700
        },
        "F5": {
            "substance": "F5",
            "amount": 700
        },
        "F6": {
            "substance": "F6",
            "amount": 700
        },
        "F7": {
            "substance": "F7",
            "amount": 700
        },
        "F8": {
            "substance": "F8",
            "amount": 700
        }
}
}

move_commands = [
    {
        "substance": "A1",
        "location": [
            "A1"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "A2",
        "location": [
            "A2"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "A3",
        "location": [
            "A3"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "A4",
        "location": [
            "A4"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "A5",
        "location": [
            "A5"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "A6",
        "location": [
            "A6"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "A7",
        "location": [
            "A7"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "A8",
        "location": [
            "A8"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "B1",
        "location": [
            "B1"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "B2",
        "location": [
            "B2"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "B3",
        "location": [
            "B3"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "B4",
        "location": [
            "B4"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "B5",
        "location": [
            "B5"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "B6",
        "location": [
            "B6"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "B7",
        "location": [
            "B7"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "B8",
        "location": [
            "B8"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "C1",
        "location": [
            "C1"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "C2",
        "location": [
            "C2"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "C3",
        "location": [
            "C3"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "C4",
        "location": [
            "C4"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "C5",
        "location": [
            "C5"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "C6",
        "location": [
            "C6"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "C7",
        "location": [
            "C7"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "C8",
        "location": [
            "C8"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "D1",
        "location": [
            "D1"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "D2",
        "location": [
            "D2"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "D3",
        "location": [
            "D3"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "D4",
        "location": [
            "D4"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "D5",
        "location": [
            "D5"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "D6",
        "location": [
            "D6"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "D7",
        "location": [
            "D7"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "D8",
        "location": [
            "D8"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "E1",
        "location": [
            "E1"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "E2",
        "location": [
            "E2"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "E3",
        "location": [
            "E3"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "E4",
        "location": [
            "E4"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "E5",
        "location": [
            "E5"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "E6",
        "location": [
            "E6"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "E7",
        "location": [
            "E7"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "E8",
        "location": [
            "E8"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "F1",
        "location": [
            "F1"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "F2",
        "location": [
            "F2"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "F3",
        "location": [
            "F3"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "F4",
        "location": [
            "F4"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "F5",
        "location": [
            "F5"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "F6",
        "location": [
            "F6"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "F7",
        "location": [
            "F7"
        ],
        "amount": 20,
        "plate": "4"
    },
    {
        "substance": "F8",
        "location": [
            "F8"
        ],
        "amount": 20,
        "plate": "4"
    }
]



class Opentrons:
    def __init__(
        self,
        protocol: protocol_api.ProtocolContext,
        deck_info: dict,
    ):
        """
        Initialise the Opentrons object.

        Parameters
        ----------
        protocol : protocol_api.ProtocolContext
            The protocol context for the current protocol.
        deck_info : dict
            Dictionary of deck information.
            Contains information of substances and their quantities on the deck.

        Returns
        -------
        None
        """
        # Set gantry speeds
        self.protocol = protocol
        # self.protocol.max_speeds["X"] = 100
        # self.protocol.max_speeds["Y"] = 100
        # self.protocol.max_speeds["Z"] = 100

        # TODO: Add dynamic loading of labware
        # self.tiprack1000 = self.protocol.load_labware(
        #     "opentrons_96_tiprack_1000ul", 1
        # )
        # self.tiprack300 = self.protocol.load_labware(
            # "opentrons_96_tiprack_300ul", 2
        # )
        self.tiprack20 = self.protocol.load_labware(
            "opentrons_96_tiprack_20ul", 2
        )
        self.plate = self.protocol.load_labware(
            "aglient_54_wellplate_2000ul", 4
        )
        self.labware = {}
        self.labware[4] = self.plate
        # self.labware[1] = self.tiprack1000
        self.labware[2] = self.tiprack20
        # Add substances to the deck
        for deck_number in deck_info:
            self.labware[int(deck_number)] = self.protocol.load_labware(
                deck_info[deck_number]["type"], int(deck_number)
            )
        # Delete name and type from deck_info
        for deck_number in deck_info:
            del deck_info[deck_number]["type"]
            del deck_info[deck_number]["name"]
        # Loading pipettes
        self.right_pipette = self.protocol.load_instrument(
            "p20_single_gen2", "right", tip_racks=[self.tiprack20]
        )
        # self.right_pipette = protocol.load_instrument(
            # "p300_single_gen2", "right", tip_racks=[self.tiprack300]
        # )
        # self.right_pipette.flow_rate.aspirate = 40
        # self.right_pipette.flow_rate.dispense = 40
        # self.right_pipette.flow_rate.aspirate = 40
        # self.right_pipette.flow_rate.dispense = 40
        # self.right_pipette.swelled = False
        self.right_pipette.swelled = False
        # For tracking substance amounts
        self.substances = defaultdict(list)
        for position in deck_info:
            position_int = int(position)
            for well_plate in deck_info[position]:
                substance_position = self.labware[position_int][well_plate]
                substance = deck_info[position][well_plate]
                substance_name = substance["substance"]
                amount = substance["amount"]
                self.substances[substance_name].append(
                    {
                        "position": substance_position,
                        "amount": amount,
                    }
                )

    def swell_tip(self, pipette, position):
        """
        Swells the tip in the `stock` labware location at a specified location.

        Notes
        -----
        Perform before a pipette is used for transfer.

        Parameters
        ----------
        pipette : pipette
            The pipette to be used.

        position:
            Position to swell the tip in.

        Returns
        -------
        None

        """
        for i in range(1):
            pipette.aspirate(3, position)
            self.protocol.delay(1)
            pipette.move_to(position.top())
            pipette.dispense(3, location=position)
        pipette.swelled = True

    def move_without_drip(self, position_to, position_from, pipette, amount):
        """
        Transfers substance from one location to another without dripping (hopefully).

        Notes
        -----
        Ideally, the swell function will be used before this function is called to reduce the
        probability of drips.

        Parameters
        ----------
        position_to: position
            Location of the target well plates to move substance to.
        position_from: position
            Location of the source well plates to move substance from.
        amount: float or int
            Amount of substance to be moved. (in uL)


        Returns
        -------
        None

        """
        # Check if pipette swelled before movement
        pipette.aspirate(amount, position_from)
        # pipette.air_gap(0)
        pipette.dispense(location=position_to.top(z=2))

    def move_substance(self, amount, substance_name, position_to, pipette):
        """
        Moves a specified amount of substance from one location to another.

        Parameters
        ----------
        amount : float or int
            Amount of substance to be moved. (in mL)
        substance_name : str
            Name of the substance to be moved.
        position_to: position
            Location of the target well plates to move substance to.
        pipette: pipette
            The pipette to be used.
        value:

        Returns
        -------
        None

        """
        # Find the deck location of the substance
        try:
            substance_position = self.substances[substance_name][0]["position"]
        except:
            pprint(self.substances)
            print(f"Substance {substance_name} not found.")
            raise RuntimeError(
                f"Substance not found in deck. This could be due to the deck being empty, or the amount of {substance_name} needed exceeding the amount placed on the deck."
            )

        # Perform swelling
        if pipette.swelled != substance_name:
            self.swell_tip(
                pipette=pipette,
                position=substance_position,
            )
            pipette.swelled = substance_name
            # Check to see if amount of substance is greater than the amount on the deck
        minimum_volume = 500
        if amount > (
            self.substances[substance_name][0]["amount"] - minimum_volume
        ):
            print(
                f"Amount of {substance_name} needed is greater than the amount on the deck.\n"
                f"Trying again to move after changing the well plate to movw from of {substance_name}."
            )
            # Change the well plate to move from
            self.substances[substance_name].pop(0)
            if len(self.substances[substance_name]) == 0:
                raise RuntimeError(
                    f"No more {substance_name} right on the deck. Please check the deck and try again."
                )
            self.move_substance(
                amount=amount,
                substance_name=substance_name,
                position_to=position_to,
                pipette=pipette,
            )

        assert pipette.swelled == substance_name
        # Get amount right on deck
        # amount_right = self.substances[substance_name][0]["amount"]
        # Change well bottom clearance to prevent pipette touching the solvent
        # aspirate_loc = substance_position.bottom()
        # aspirate_loc = aspirate_loc.move(
        #     Point(0, 0, -aspirate_loc.point.z + 1)
        # )
        self.move_without_drip(
            pipette=pipette,
            position_to=position_to,
            position_from=substance_position,
            amount=amount,
        )
        self.substances[substance_name][0]["amount"] -= amount


def run(protocol: protocol_api.ProtocolContext):
    """
    Run the protocol.
    """

    amount_added = defaultdict(lambda: 0)
    substance_path = substance_locations
    move_path = move_commands
    # Check if root in the directory
    #if not substance_path.is_file():
    #    substance_path = Path("/root/Opentrons_Code/MS_transfer/substance_locations.json")
    #    move_path = Path("/root/Opentrons_Code/MS_transfer/move_commands.json")
    #assert "MS_transfer" in str(substance_path.absolute())
    #with open(str(substance_path)) as f:
    #    deck_info = json.load(f)
    ot = Opentrons(protocol=protocol, deck_info=substance_locations)

    #with open(str(move_path)) as f:
    #    move_info = json.load(f)

    # Extract list of moves from the move information
    moves = []
    for substance in move_commands:
        for location in substance["location"]:
            moves.append(
                {
                    "substance": substance["substance"],
                    "location": location,
                    "amount": substance["amount"],
                    "plate": substance["plate"],
                }
            )
    added_substances = []
    positions_added = defaultdict(str)
    pipette_max_volume = 20
    for move in moves:
        location = move["location"]
        amount = int(move["amount"])
        plate = int(move["plate"])
        substance = move["substance"]
        # Get target well location
        target_well = ot.labware[plate].wells(location)[0]
        # Add the first substance to the list
        num_moves = amount // pipette_max_volume
        added = 0
        if len(added_substances) == 0:
            ot.right_pipette.pick_up_tip()
            added_substances.append(substance)
        # Check if substance matches the last substance added
        elif substance != added_substances[-1]:
            # Get a new tip
            ot.right_pipette.drop_tip()
            ot.right_pipette.pick_up_tip()
            added_substances.append(substance)
        if num_moves == 1:
            num_moves = 0
        for i in range(num_moves + 1):
            # Check if move is the last move
            if i == num_moves:
                amount_to_add = amount - added
            else:
                amount_to_add = pipette_max_volume
            ot.move_substance(
                amount=amount_to_add,
                substance_name=substance,
                position_to=target_well,
                pipette=ot.right_pipette,
            )
            added += amount_to_add
            amount_added[location] += amount_to_add
        positions_added[location] += substance + " "
    for line in protocol.commands():
        continue
    pprint(amount_added)
    pprint(positions_added)
