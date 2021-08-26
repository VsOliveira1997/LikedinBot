
local npc = getCreatureByName("Yasir")

if not npc then 

  return false 

end

if retries > 10 then

  return false

end

local pos = player:getPosition()

local npcPos = npc:getPosition()

if math.max(math.abs(pos.x - npcPos.x), math.abs(pos.y - npcPos.y)) > 3 then

  autoWalk(npcPos, {precision=3})

  delay(300)

  return "retry"

end

if not NPC.isTrading() then

  NPC.say("hi")

  NPC.say("trade")

  delay(200)

  return "retry"

end

NPC.sell(10304)
NPC.sell(5911)
NPC.sell(21974)
NPC.sell(21975)
schedule(1000, function()

  -- buy again in 1s

  NPC.sell(8061)
  NPC.sell(5911)
  NPC.sell(21974) 
  NPC.sell(21975)

  NPC.closeTrade()

  NPC.say("bye")

end)

delay(1200)

return true

