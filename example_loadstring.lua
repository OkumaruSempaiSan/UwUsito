local Params = {
    RepoURL = "https://raw.githubusercontent.com/OkumaruSempaiSan/UwUsito/main/",
    SSI = "saveinstance",
} 

local synsaveinstance = loadstring(game:HttpGet(Params.RepoURL .. Params.SSI .. ".luau", true), Params.SSI)()

local Options = {
    Decompile = false,
    SaveBytecode = false,
    scriptcache = false,
}

synsaveinstance(Options)
