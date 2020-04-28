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
		"Password": "jv357159",
		"Port": "5432",
		"Driver":"pygresql"
	},
	"Mainserver": {
		"Port": int("7002")
	}
}