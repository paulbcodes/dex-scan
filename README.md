# Flask app for displaying dex pairings / new dex pairings

Presently this is set for a no longer acive testnet which would require changing for your own purposes. Contract addresses would need changing to any chain you choose to use it on also. It will work for pancakeswap or any of its forks, the abis would need changing for any other dex type.

Supplied with a a dataset that can be used to see an active website without making any changes (although no new pairs will display as the current rpc and dex is not active any more). For your own use you should delete the .db file so your own is created.

To see the website running simply pip install the requirements.txt file and then type python3 main.py - this will display a working website using my dataset.

For full useage you will need to add current pairs you want added to the list in add2db.py, this will create your database with the pairs you added top the list. Once that program has populated the database you can run python3 main.py to see your website. nce active python3 newpairs.py which will then add any new dex listings to your databse and display them on the frontend.
