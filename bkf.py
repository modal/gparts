import webbrowser

links=["https://bkingsfirearms.com/shop/magazines/lancer-l5awm-300-blk-20rd-trans-smoke/",
       "https://bkingsfirearms.com/shop/gas-tubes-blocks-and-muzzle-brakes-flash-hiders/kvp-mach-linear-comp-thread-adapter-5-8x24/",
       "https://bkingsfirearms.com/shop/gas-tubes-blocks-and-muzzle-brakes-flash-hiders/kvp-mach-linear-comp-thread-adapter-1-2x28/",
       "https://bkingsfirearms.com/shop/gas-tubes-blocks-and-muzzle-brakes-flash-hiders/kvp-mach-linear-comp-end-cap/",
       "https://bkingsfirearms.com/shop/gas-tubes-blocks-and-muzzle-brakes-flash-hiders/kvp-mach-linear-comp-end-cap-flash-hider/",
       "https://bkingsfirearms.com/shop/gas-tubes-blocks-and-muzzle-brakes-flash-hiders/kvp-mach-3-modular-linear-comp-body/",
       "https://bkingsfirearms.com/shop/ar15-barrels-223-wylde-5-56mm-300-blk-and-6-5-grendel/bkf-ar15-16%e2%80%b3-300-blk-drp-profile-pistol-length-4150-cmv-1-7-twist-barrel-w-pinned-gas-block/",
       "https://bkingsfirearms.com/shop/ar15-lower-receiver-parts-kits/bkf-m4-mod-0-standard-power-rifle-buffer-tube-assembly/",
       "https://bkingsfirearms.com/shop/ar15-upper-receiver-parts-kits/ar15-mil-spec-upper-parts-kit/",
       "https://bkingsfirearms.com/shop/gas-tubes-blocks-and-muzzle-brakes-flash-hiders/bkf-750-low-profile-gas-block/",
       "https://bkingsfirearms.com/shop/gas-tubes-blocks-and-muzzle-brakes-flash-hiders/bkf-750-low-profile-gas-block-stainless-steel/",
       "https://bkingsfirearms.com/shop/gas-tubes-blocks-and-muzzle-brakes-flash-hiders/bkf-nitride-750-gas-block-and-ss-tube-mid/",
       "https://bkingsfirearms.com/shop/gas-tubes-blocks-and-muzzle-brakes-flash-hiders/bkf-nitride-750-gas-block-and-ss-melonite-tube-mid/",
       "https://bkingsfirearms.com/shop/gas-tubes-blocks-and-muzzle-brakes-flash-hiders/bkf-nitride-750-gas-block-and-ss-melonite-tube-rifle/",
       "https://bkingsfirearms.com/shop/ar15handguards/bkf-m4-mod-0-15-25-m-lok-handguard/",
       "https://bkingsfirearms.com/shop/ar15handguards/bkf-m5-lr308-15-m-lok-handguard/",
       "https://bkingsfirearms.com/shop/ar15handguards/bkf-ar15-7-m-lok-handguard/",
       "https://bkingsfirearms.com/shop/ar15handguards/bkf-ar15-9-875-m-lok-handguard/",
       "https://bkingsfirearms.com/shop/ar15handguards/bkf-ar15-13-m-lok-handguard/",
       "https://bkingsfirearms.com/shop/ar15-lower-receiver-parts-kits/bkf-ar15-ejection-port-cover-rod-c-clip/"
       "https://bkingsfirearms.com/shop/gas-tubes-blocks-and-muzzle-brakes-flash-hiders/2bo-double-port-muzzle-brake-outside-threaded-223-5-56/",
       "https://bkingsfirearms.com/shop/gas-tubes-blocks-and-muzzle-brakes-flash-hiders/bkf-m4-mod-1-300-blk-6-5-grendel-comp/",
       "https://bkingsfirearms.com/shop/gas-tubes-blocks-and-muzzle-brakes-flash-hiders/bkf-m4-mod-0-full-power-5-56-223-comp/",
       "https://bkingsfirearms.com/shop/gas-tubes-blocks-and-muzzle-brakes-flash-hiders/bkf-m4-mod-1-5-56-223-extended-comp/",
       "https://bkingsfirearms.com/shop/gas-tubes-blocks-and-muzzle-brakes-flash-hiders/bkf-ar15-5-56-223-a2-flash-hider-nitride-w-crush-washer/"]

#wb=webbrowser.Mozilla("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
wb=webbrowser.Chrome("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")


for x in links:
    wb.open(x)
