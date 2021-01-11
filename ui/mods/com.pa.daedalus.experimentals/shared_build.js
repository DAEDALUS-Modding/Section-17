var newBuild = {
"/pa/units/PAEIOU/experimental_vehicle_gantry/experimental_vehicle_gantry.json": ["gantry", 0,{ row: 0, column: 4, titans: true }],
"/pa/units/PAEIOU/big_bill/big_bill.json": ["vehicle", 0,{ row: 0, column: 4, titans: true }],
"/pa/units/PAEIOU/pineapple/pineapple.json": ["bot", 0,{ row: 0, column: 5, titans: true }],
"/pa/units/PAEIOU/floater/floater.json": ["vehicle", 0,{ row: 0, column: 1, titans: true }],

}
if (Build && Build.HotkeyModel && Build.HotkeyModel.SpecIdToGridMap) {
_.extend(Build.HotkeyModel.SpecIdToGridMap, newBuild);
}