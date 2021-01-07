var newBuild = {
    "/pa/units/pandapack/swole_stinger/swole_stinger.json": ["bot", 0, { row: 1, column: 7 }],
    "/pa/units/pandapack/vehicle_chaddriffter/vehicle_chaddriffter.json": ["vehicle", 0, { row: 0, column: 1 }],
    "/pa/units/pandapack/pineapple/bot_radarpineapple.json": ["bot", 0, { row: 0, column: 1 }],
    "/pa/units/pandapack/titan_yandercannon/titan_yandercannon.json": ["vehicle", 0, { row: 0, column: 2 }]

}
if (Build && Build.HotkeyModel && Build.HotkeyModel.SpecIdToGridMap) {
    _.extend(Build.HotkeyModel.SpecIdToGridMap, newBuild);
}