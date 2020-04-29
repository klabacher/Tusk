import sys
config = {
	"REDIS-DB": {
		"Address": "localhost",
		"DB": "0",
		"Password": None,
		"Port": "6379"
	},
	"Database": {
        "Address": "localhost",
		"User":"postgres",
		"DB": "houdini",
		"Password": "",
		"Port": "5432",
		"Driver":"psycopg2"
	},
	"Mainserver": {
		"Port": int("7002")
	}
}
