from src.ATMNodeOrdering import ATMNodeOrdering

class SearchEngine():
    def __init__(this, aBot, aDataCollector):
        this.bot = aBot
        this.nodeOrdering = ATMNodeOrdering(aDataCollector)

    def deploySearch(this, update, context):
        this.bot.setCurrentSearchEngine(this)
        this.bot.deploySearchForValidSearch(update, context, this)
        
    def validATMs(this, long, lat):
        inRangeATMIndexes, atmData = this.nodeOrdering.closestNodes(long, lat)
        return inRangeATMIndexes, atmData