from ATMNodeOrdering import ATMNodeOrdering

class SearchEngine:
    def __init__(this, aBot):
        this.bot = aBot
        
    def deploySearch(this, update, context):
        raise NotImplementedError("Please Implement This Method")
    
    def validATMs(this, long, lat):
        raise NotImplementedError("Please Implement This Method")


class NullSearchEngine(SearchEngine):
    def __init__(this, aBot):
        super().__init__(aBot)

    def deploySearch(this, update, context):
        this.bot.deploySearchForNullSearch(update, context)

    def validATMs(this, long, lat):
        this.bot.deployValidATMsForNullSearch()
        return []


class ValidSearchEngine(SearchEngine):
    def __init__(this, aBot, aDataCollector):
        super().__init__(aBot)
        this.nodeOrdering = ATMNodeOrdering(aDataCollector)

    def deploySearch(this, update, context):
        this.bot.setCurrentSearchEngine(this)
        this.bot.deploySearchForValidSearch(update, context, this)
        
    def validATMs(this, long, lat):
        return this.nodeOrdering.closestNodes(long, lat)